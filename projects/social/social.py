class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # create array with all possible friendships
        possible_friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                possible_friendship = (user, friend)
                possible_friendships.append(possible_friendship)
                
        # then shuffle it randomly and only take as many as we need
        random.shuffle(possible_friendships)
        # and add those friendships since we 
        total_friendships = num_users * avg_friendships // 2
        random_friendships = possible_friendships[:total_friendships]

        # only need an avg num of friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def get_friendships(self, user_id):
        return self.friendships[user_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # bfs, because we want the shortest friendship path

        queue = Queue()

        path = [user_id]
        queue.enqueue(path)

        while queue.size() > 0:
            current_path = queue.dequeue()
            new_user_id = current_path[-1]

            if new_user_id not in visited:
                # the first time we come across them using bfs
                # IS the shortest path to that user, so just store that
                visited[new_user_id] = current_path

                friends = self.get_friendships(new_user_id)
                for friend in friends:
                    path_copy = list(path)
                    path_copy.append(friend)
                    queue.enqueue(path_copy)

        return visited

# what's the average degree of separation between a user and their extended network?
# you could add up all the path lengths for each user 
# and then divide them by how many friends this person has (connections)

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # figuring out average degree of separation
    total_paths_length = 0
    for user_id in connections:
        total_paths_length += len(connections[user_id])
    average_degree_of_separation = total_paths_length / len(connections)    
    print("average degree of separation: ", average_degree_of_separation)
    print(connections)
