from collections import defaultdict, deque

class EventScheduler:
    def __init__(self):
        self.graph = defaultdict(list)  # adjacency list representation of the DAG
        self.in_degree = defaultdict(int)  # in-degree (number of dependencies) for each task

    def add_task(self, task_id, depends_on):
        """Add a task with its dependencies to the graph."""
        if task_id not in self.in_degree:
            self.in_degree[task_id] = 0
        for dependency in depends_on:
            self.graph[dependency].append(task_id)
            self.in_degree[task_id] += 1

    def topological_sort(self):
        """Return tasks in topologically sorted order."""
        zero_in_degree_queue = deque([task for task in self.in_degree if self.in_degree[task] == 0])
        topological_order = []

        while zero_in_degree_queue:
            task = zero_in_degree_queue.popleft()
            topological_order.append(task)

            # For each dependent task, reduce in-degree and if it becomes 0, add to queue
            for dependent in self.graph[task]:
                self.in_degree[dependent] -= 1
                if self.in_degree[dependent] == 0:
                    zero_in_degree_queue.append(dependent)

        if len(topological_order) == len(self.in_degree):
            return topological_order
        else:
            raise Exception("Cycle detected in task dependencies")

