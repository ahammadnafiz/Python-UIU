from jsonplaceholder_client import JSONPlaceholderClient, Post, Comment, User
import argparse
import json
import os
from typing import Any, Dict, List
from tabulate import tabulate 


class JSONPlaceholderDemo:
    """Demo application for the JSONPlaceholder API client."""
    
    def __init__(self, cache_enabled: bool = True):
        self.client = JSONPlaceholderClient(cache_enabled=cache_enabled)
    
    def display_menu(self):
        """Display the main menu options."""
        print("\n===== JSONPlaceholder API Client Demo =====")
        print("1. Get all posts")
        print("2. Get a specific post")
        print("3. Get comments for a post")
        print("4. Create a new post")
        print("5. Update a post")
        print("6. Delete a post")
        print("7. Get all users")
        print("8. View user's todos")
        print("9. Get user's albums and photos")
        print("10. Search posts by user")
        print("11. Advanced query")
        print("12. Export data to JSON")
        print("0. Exit")
        print("=========================================")
    
    def print_table(self, data: List[Dict], keys: List[str] = None):
        """Print data as a formatted table."""
        if not data:
            print("No data to display.")
            return
        
        if not keys:
            # Use all keys from the first item
            keys = list(data[0].keys())
        
        # Prepare rows
        rows = []
        for item in data:
            row = []
            for key in keys:
                value = item.get(key, "")
                # Truncate long text fields
                if isinstance(value, str) and len(value) > 50:
                    value = value[:47] + "..."
                row.append(value)
            rows.append(row)
        
        print(tabulate(rows, headers=keys, tablefmt="grid"))
    
    def get_all_posts(self):
        """Get and display all posts."""
        try:
            posts = self.client.get_resource("posts")
            self.print_table(posts, ["id", "userId", "title"])
            print(f"\nTotal posts: {len(posts)}")
        except Exception as e:
            print(f"Error fetching posts: {e}")
    
    def get_post(self):
        """Get and display a specific post."""
        try:
            post_id = int(input("Enter post ID: "))
            post = self.client.get_resource("posts", post_id)
            print("\n----- Post Details -----")
            print(f"ID: {post['id']}")
            print(f"User ID: {post['userId']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
        except ValueError:
            print("Please enter a valid post ID.")
        except Exception as e:
            print(f"Error fetching post: {e}")
    
    def get_post_comments(self):
        """Get and display comments for a specific post."""
        try:
            post_id = int(input("Enter post ID: "))
            comments = self.client.get_resource("posts", post_id, "comments")
            print(f"\nComments for post {post_id}:")
            self.print_table(comments, ["id", "name", "email"])
            print(f"\nTotal comments: {len(comments)}")
        except ValueError:
            print("Please enter a valid post ID.")
        except Exception as e:
            print(f"Error fetching comments: {e}")
    
    def create_post(self):
        """Create a new post."""
        try:
            user_id = int(input("Enter user ID: "))
            title = input("Enter post title: ")
            body = input("Enter post body: ")
            
            new_post = Post(userId=user_id, id=None, title=title, body=body)
            created_post = self.client.create_resource("posts", new_post.to_dict())
            
            print("\n----- Created Post -----")
            print(f"ID: {created_post['id']}")
            print(f"User ID: {created_post['userId']}")
            print(f"Title: {created_post['title']}")
            print(f"Body: {created_post['body']}")
            print("Note: In JSONPlaceholder, new resources aren't actually created on the server but are simulated as if they were.")
        except ValueError:
            print("Please enter a valid user ID.")
        except Exception as e:
            print(f"Error creating post: {e}")
    
    def update_post(self):
        """Update an existing post."""
        try:
            post_id = int(input("Enter post ID to update: "))
            
            # Get the current post
            try:
                current_post = self.client.get_resource("posts", post_id)
            except:
                print(f"Post with ID {post_id} not found.")
                return
                
            # Get update fields
            print("\nLeave field empty to keep current value:")
            title = input(f"Title [{current_post['title']}]: ")
            body = input(f"Body [{current_post['body']}]: ")
            
            # Use current values if fields are empty
            if not title:
                title = current_post['title']
            if not body:
                body = current_post['body']
                
            # Create update data
            update_data = {
                'userId': current_post['userId'],
                'title': title,
                'body': body
            }
            
            # Ask if partial or full update
            update_type = input("Partial update (PATCH) or full update (PUT)? [patch/put]: ").lower()
            is_patch = update_type != "put"
            
            updated_post = self.client.update_resource("posts", post_id, update_data, patch=is_patch)
            
            print("\n----- Updated Post -----")
            print(f"ID: {updated_post['id']}")
            print(f"User ID: {updated_post['userId']}")
            print(f"Title: {updated_post['title']}")
            print(f"Body: {updated_post['body']}")
            print("Note: In JSONPlaceholder, updates aren't actually saved on the server but are simulated.")
        except ValueError:
            print("Please enter a valid post ID.")
        except Exception as e:
            print(f"Error updating post: {e}")
    
    def delete_post(self):
        """Delete a post."""
        try:
            post_id = int(input("Enter post ID to delete: "))
            self.client.delete_resource("posts", post_id)
            print(f"Post {post_id} has been deleted.")
            print("Note: In JSONPlaceholder, deletions aren't actually permanent on the server but are simulated.")
        except ValueError:
            print("Please enter a valid post ID.")
        except Exception as e:
            print(f"Error deleting post: {e}")
    
    def get_all_users(self):
        """Get and display all users."""
        try:
            users = self.client.get_resource("users")
            self.print_table(users, ["id", "name", "email", "username"])
            print(f"\nTotal users: {len(users)}")
        except Exception as e:
            print(f"Error fetching users: {e}")
    
    def view_user_todos(self):
        """View todos for a specific user."""
        try:
            user_id = int(input("Enter user ID: "))
            
            # Get user info
            try:
                user = self.client.get_resource("users", user_id)
                print(f"\nTodos for {user['name']}:")
            except:
                print(f"User with ID {user_id} not found.")
                return
            
            # Get user's todos
            todos = self.client.get_resource("todos", query_params={"userId": user_id})
            
            # Count completed vs not completed
            completed = sum(1 for todo in todos if todo["completed"])
            not_completed = len(todos) - completed
            
            self.print_table(todos, ["id", "title", "completed"])
            print(f"\nTotal todos: {len(todos)}")
            print(f"Completed: {completed}")
            print(f"Not completed: {not_completed}")
            print(f"Completion rate: {(completed / len(todos) * 100):.1f}%")
        except ValueError:
            print("Please enter a valid user ID.")
        except Exception as e:
            print(f"Error fetching todos: {e}")
    
    def get_user_albums_and_photos(self):
        """Get albums and photos for a specific user."""
        try:
            user_id = int(input("Enter user ID: "))
            
            # Get user info
            try:
                user = self.client.get_resource("users", user_id)
                print(f"\nAlbums for {user['name']}:")
            except:
                print(f"User with ID {user_id} not found.")
                return
            
            # Get user's albums
            albums = self.client.get_resource("albums", query_params={"userId": user_id})
            self.print_table(albums, ["id", "title"])
            
            # Ask if user wants to see photos from a specific album
            album_id = input("\nEnter album ID to see photos (or press Enter to skip): ")
            if album_id:
                try:
                    album_id = int(album_id)
                    album = next((a for a in albums if a["id"] == album_id), None)
                    
                    if not album:
                        print(f"Album with ID {album_id} not found for this user.")
                        return
                        
                    photos = self.client.get_resource("albums", album_id, "photos")
                    print(f"\nPhotos in album '{album['title']}':")
                    self.print_table(photos, ["id", "title", "thumbnailUrl"])
                    print(f"\nTotal photos: {len(photos)}")
                except ValueError:
                    print("Please enter a valid album ID.")
        except ValueError:
            print("Please enter a valid user ID.")
        except Exception as e:
            print(f"Error fetching albums/photos: {e}")
    
    def search_posts_by_user(self):
        """Search posts by user ID."""
        try:
            user_id = int(input("Enter user ID: "))
            
            # Get user info
            try:
                user = self.client.get_resource("users", user_id)
                print(f"\nPosts by {user['name']}:")
            except:
                print(f"User with ID {user_id} not found.")
                return
            
            # Get user's posts
            posts = self.client.get_resource("posts", query_params={"userId": user_id})
            self.print_table(posts, ["id", "title"])
            print(f"\nTotal posts: {len(posts)}")
        except ValueError:
            print("Please enter a valid user ID.")
        except Exception as e:
            print(f"Error searching posts: {e}")
    
    def advanced_query(self):
        """Perform advanced queries on the API."""
        print("\n----- Advanced Query Options -----")
        print("1. Find posts with specific title keywords")
        print("2. Count comments per post")
        print("3. Find users with most posts")
        print("4. Find users with most todos")
        print("5. Back to main menu")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                self._find_posts_by_keyword()
            elif choice == 2:
                self._count_comments_per_post()
            elif choice == 3:
                self._find_users_with_most_posts()
            elif choice == 4:
                self._find_users_with_most_todos()
            elif choice == 5:
                return
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")
        except Exception as e:
            print(f"Error in advanced query: {e}")
    
    def _find_posts_by_keyword(self):
        """Find posts containing specific keywords in title or body."""
        keyword = input("Enter keyword to search in post titles/bodies: ").lower()
        
        # Get all posts
        posts = self.client.get_resource("posts")
        
        # Filter posts containing the keyword
        matching_posts = [
            post for post in posts 
            if keyword in post["title"].lower() or keyword in post["body"].lower()
        ]
        
        if matching_posts:
            self.print_table(matching_posts, ["id", "userId", "title"])
            print(f"\nFound {len(matching_posts)} posts containing '{keyword}'")
        else:
            print(f"No posts found containing '{keyword}'")
    
    def _count_comments_per_post(self):
        """Count the number of comments for each post."""
        # Get all posts
        posts = self.client.get_resource("posts")
        
        # Get comments for each post
        post_stats = []
        for post in posts[:10]:  # Limit to 10 posts to avoid too many API calls
            post_id = post["id"]
            comments = self.client.get_resource("posts", post_id, "comments")
            post_with_count = {
                "id": post_id,
                "title": post["title"],
                "comment_count": len(comments)
            }
            post_stats.append(post_with_count)
        
        # Sort by comment count (descending)
        post_stats.sort(key=lambda x: x["comment_count"], reverse=True)
        
        # Display results
        self.print_table(post_stats, ["id", "title", "comment_count"])
    
    def _find_users_with_most_posts(self):
        """Find users with the most posts."""
        # Get all posts
        posts = self.client.get_resource("posts")
        
        # Count posts per user
        user_post_counts = {}
        for post in posts:
            user_id = post["userId"]
            user_post_counts[user_id] = user_post_counts.get(user_id, 0) + 1
        
        # Get user details
        users = self.client.get_resource("users")
        
        # Create user stats
        user_stats = []
        for user in users:
            user_id = user["id"]
            user_stats.append({
                "id": user_id,
                "name": user["name"],
                "post_count": user_post_counts.get(user_id, 0)
            })
        
        # Sort by post count (descending)
        user_stats.sort(key=lambda x: x["post_count"], reverse=True)
        
        # Display results
        self.print_table(user_stats, ["id", "name", "post_count"])
    
    def _find_users_with_most_todos(self):
        """Find users with the most todos."""
        # Get all todos
        todos = self.client.get_resource("todos")
        
        # Count todos per user and track completion
        user_todo_counts = {}
        user_completed_counts = {}
        
        for todo in todos:
            user_id = todo["userId"]
            user_todo_counts[user_id] = user_todo_counts.get(user_id, 0) + 1
            if todo["completed"]:
                user_completed_counts[user_id] = user_completed_counts.get(user_id, 0) + 1
        
        # Get user details
        users = self.client.get_resource("users")
        
        # Create user stats
        user_stats = []
        for user in users:
            user_id = user["id"]
            total_todos = user_todo_counts.get(user_id, 0)
            completed_todos = user_completed_counts.get(user_id, 0)
            completion_rate = (completed_todos / total_todos * 100) if total_todos > 0 else 0
            
            user_stats.append({
                "id": user_id,
                "name": user["name"],
                "todo_count": total_todos,
                "completed": completed_todos,
                "completion_rate": f"{completion_rate:.1f}%"
            })
        
        # Sort by todo count (descending)
        user_stats.sort(key=lambda x: x["todo_count"], reverse=True)
        
        # Display results
        self.print_table(user_stats, ["id", "name", "todo_count", "completed", "completion_rate"])
    
    def export_data(self):
        """Export data to JSON files."""
        print("\n----- Export Options -----")
        print("1. Export all posts")
        print("2. Export all comments")
        print("3. Export all users")
        print("4. Export all todos")
        print("5. Export everything")
        print("6. Back to main menu")
        
        try:
            choice = int(input("Enter your choice: "))
            
            # Create export directory if it doesn't exist
            os.makedirs("exports", exist_ok=True)
            
            if choice == 1:
                posts = self.client.get_resource("posts")
                with open("exports/posts.json", "w") as f:
                    json.dump(posts, f, indent=2)
                print(f"Exported {len(posts)} posts to exports/posts.json")
            elif choice == 2:
                comments = self.client.get_resource("comments")
                with open("exports/comments.json", "w") as f:
                    json.dump(comments, f, indent=2)
                print(f"Exported {len(comments)} comments to exports/comments.json")
            elif choice == 3:
                users = self.client.get_resource("users")
                with open("exports/users.json", "w") as f:
                    json.dump(users, f, indent=2)
                print(f"Exported {len(users)} users to exports/users.json")
            elif choice == 4:
                todos = self.client.get_resource("todos")
                with open("exports/todos.json", "w") as f:
                    json.dump(todos, f, indent=2)
                print(f"Exported {len(todos)} todos to exports/todos.json")
            elif choice == 5:
                print("Exporting all data. This may take a moment...")
                all_resources = self.client.get_all_resources()
                for resource, data in all_resources.items():
                    with open(f"exports/{resource}.json", "w") as f:
                        json.dump(data, f, indent=2)
                    print(f"Exported {len(data)} {resource} to exports/{resource}.json")
            elif choice == 6:
                return
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")
        except Exception as e:
            print(f"Error exporting data: {e}")
    
    def run(self):
        """Run the demo application."""
        while True:
            self.display_menu()
            try:
                choice = input("Enter your choice: ")
                
                if choice == "1":
                    self.get_all_posts()
                elif choice == "2":
                    self.get_post()
                elif choice == "3":
                    self.get_post_comments()
                elif choice == "4":
                    self.create_post()
                elif choice == "5":
                    self.update_post()
                elif choice == "6":
                    self.delete_post()
                elif choice == "7":
                    self.get_all_users()
                elif choice == "8":
                    self.view_user_todos()
                elif choice == "9":
                    self.get_user_albums_and_photos()
                elif choice == "10":
                    self.search_posts_by_user()
                elif choice == "11":
                    self.advanced_query()
                elif choice == "12":
                    self.export_data()
                elif choice == "0":
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JSONPlaceholder API Demo")
    parser.add_argument("--no-cache", action="store_true", help="Disable caching")
    args = parser.parse_args()
    
    demo = JSONPlaceholderDemo(cache_enabled=not args.no_cache)
    demo.run()