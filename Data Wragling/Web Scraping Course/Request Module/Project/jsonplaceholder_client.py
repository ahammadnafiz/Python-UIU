import requests
import json
import os
from typing import Dict, List, Union, Optional, Any
import time

class JSONPlaceholderClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    RESOURCES = {
        "posts": "/posts",
        "comments": "/comments",
        "albums": "/albums",
        "photos": "/photos",
        "todos": "/todos",
        "users": "/users"
    }

    def __init__(self, cache_enabled: bool = True,
                 cache_dir: str = "cache"):
        self.session = requests.Session()
        self.cache_enabled = cache_enabled
        self.cache_dir = cache_dir

        if self.cache_enabled:
            os.makedirs(self.cache_dir, exist_ok=True)

    def _get_cache_path(self, resource: str, resource_id: Optional[int] = None, 
                       related_resource: Optional[str] = None) -> str:
        
        if resource_id is not None and related_resource is not None:
            return os.path.join(self.cache_dir, f"{resource}_{resource_id}_{related_resource}.json")
        elif resource_id is not None:
            return os.path.join(self.cache_dir, f"{resource}_{resource_id}.json")
        else:
            return os.path.join(self.cache_dir, f"{resource}.json")
        
    def _get_from_cache(self, cache_path: str) -> Optional[Dict]:
        
        if not self.cache_enabled:
            return None
            
        try:
            if os.path.exists(cache_path):
                with open(cache_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Cache error: {e}")
        return None
    
    def _save_to_cache(self, cache_path: str, data: Any) -> None:
        
        if not self.cache_enabled:
            return
            
        try:
            with open(cache_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Cache write error: {e}")

    def get_resource(self, resource: str, resource_id: Optional[int] = None,
                   related_resource: Optional[str] = None, query_params: Optional[Dict] = None) -> Any:
        """
        Get resources from the API with optional filtering.
        
        Args:
            resource: The resource to fetch (posts, comments, etc.)
            resource_id: Optional ID to fetch a specific resource
            related_resource: Optional related resource (e.g. comments for a post)
            query_params: Optional query parameters for filtering
            
        Returns:
            The requested resource data
        """

        if resource not in self.RESOURCES:
            raise ValueError(f"Invalid resource '{resource}'. Available resources: {', '.join(self.RESOURCES.keys())}")
        
        url = f"{self.BASE_URL}{self.RESOURCES[resource]}"

        if resource_id is not None:
            url = f"{url}/{resource_id}"

        if related_resource is not None:
            if related_resource not in self.RESOURCES:
                raise ValueError(f"Invalid related resource '{related_resource}'. Available resources: {', '.join(self.RESOURCES.keys())}")
            url = f"{url}/{self.RESOURCES[related_resource]}"

        cache_path = self._get_cache_path(resource, resource_id, related_resource)
        cached_data = self._get_from_cache(cache_path)

        if cached_data is not None:
            return cached_data
        
        # Make the request
        response = self.session.get(url, params=query_params)
        response.raise_for_status()
        data = response.json()

        self._save_to_cache(cache_path, data)
        return data
    
    def create_resource(self, resource: str, data: Dict) -> Dict:
        """
        Create a new resource.
        
        Args:
            resource: The resource type to create
            data: The data for the new resource
            
        Returns:
            The created resource data
        """

        if resource not in self.RESOURCES:
            raise ValueError(f"Invalid resource '{resource}'. Available resources: {', '.join(self.RESOURCES.keys())}")
        
        url = f"{self.BASE_URL}{self.RESOURCES[resource]}"
        
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def update_resource(self, resource: str, resource_id: int, data: Dict, patch: bool = False) -> Dict:
        """
        Update an existing resource.
        
        Args:
            resource: The resource type to update
            resource_id: The ID of the resource to update
            data: The updated data
            patch: Whether to perform a PATCH (partial update) instead of PUT
            
        Returns:
            The updated resource data
        """
        
        if resource not in self.RESOURCES:
            raise ValueError(f"Invalid resource '{resource}'. Available resources: {', '.join(self.RESOURCES.keys())}")
        
        url = f"{self.BASE_URL}{self.RESOURCES[resource]}/{resource_id}"
        
        if patch:
            response = self.session.patch(url, json=data)
        else:
            response = self.session.put(url, json=data)
            
        response.raise_for_status()

        # Invalidate cache
        cache_path = self._get_cache_path(resource, resource_id)
        if os.path.exists(cache_path):
            os.remove(cache_path)

        return response.json()

    def delete_resource(self, resource: str, resource_id: int) -> Dict:
        """
        Delete a resource.
        
        Args:
            resource: The resource type to delete
            resource_id: The ID of the resource to delete
            
        Returns:
            The response data (usually empty)
        """
        if resource not in self.RESOURCES:
            raise ValueError(f"Invalid resource: {resource}")
        
        url = f"{self.BASE_URL}{self.RESOURCES[resource]}/{resource_id}"
        response = self.session.delete(url)
        response.raise_for_status()

        # Invalidate cache
        cache_path = self._get_cache_path(resource, resource_id)
        if os.path.exists(cache_path):
            os.remove(cache_path)

        return response.json()
    
    def get_all_resources(self) -> Dict[str, List]:
        """
        Fetch all resources from the API.
        
        Returns:
            A dictionary containing all resources
        """
        all_resources = {}
        
        for resource in self.RESOURCES:
            print(f"Fetching {resource}...")
            all_resources[resource] = self.get_resource(resource)
            # Be nice to the API - add a small delay between requests
            time.sleep(0.1)
            
        return all_resources


class Post:
    def __init__(self, userId: int, id: Optional[int], title: str, body: str):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body

    @classmethod
    def from_dict(cls, data: Dict) -> "Post":
        return cls(data["userId"], data["id"], data["title"], data["body"])
    
    def to_dict(self) -> Dict:
        return {
            "userId": self.userId,
            "id": self.id,
            "title": self.title,
            "body": self.body
        }
    
    def __repr__(self):
        return f"<Post {self.id}: {self.title}>"
    

class Comment:
    def __init__(self, postId: int, id: Optional[int], name: str, email: str, body: str):
        self.postId = postId
        self.id = id
        self.name = name
        self.email = email
        self.body = body

    @classmethod
    def from_dict(cls, data: Dict) -> "Comment":
        return cls(data["postId"], data["id"], data["name"], data["email"], data["body"])
    
    def to_dict(self) -> Dict:
        return {
            "postId": self.postId,
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "body": self.body
        }
    
    def __repr__(self):
        return f"<Comment {self.id}: {self.name}>"
    

class User:
    def __init__(self, id: Optional[int], name: str, username: str, email: str, 
                 address: Dict, phone: str, website: str, company: Dict):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    @classmethod
    def from_dict(cls, data: Dict) -> "User":
        return cls(data["id"], data["name"], data["username"], data["email"], 
                   data["address"], data["phone"], data["website"], data["company"])
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "company": self.company
        }
    
    def __repr__(self):
        return f"<User {self.id}: {self.name}>"