<template>
  <div>
    <h3>Task List</h3>

    <!-- Button to fetch sorted tasks by priority -->
    <button @click="fetchSortedTasks" class="btn btn-secondary mb-3">
      Sort by Priority
    </button>

    <!-- Display a message if there are no tasks -->
    <p v-if="tasks.length === 0">No tasks available. Please add some tasks.</p>

    <!-- Display the tasks -->
    <ul class="list-group">
      <li v-for="task in tasks" :key="task.id" class="list-group-item d-flex justify-content-between align-items-center">
        <div>
          <strong>{{ task.title }}</strong> - {{ task.priority }}
          <br />
          <em></em> {{ task.description || 'No description provided' }}
          <br />
          <span class="badge bg-info">Status: {{ task.status }}</span>
        </div>
        <!-- Action Buttons -->
        <div>
          <button @click="editTask(task)" class="btn btn-sm btn-warning me-2">Update</button>
          <button @click="deleteTask(task.id)" class="btn btn-sm btn-danger">Delete</button>
        </div>
      </li>
    </ul>

    <!-- Loading message -->
    <p v-if="isLoading">Loading tasks...</p>

    <!-- Error message -->
    <p v-if="errorMessage" class="text-danger">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tasks: [], // Store tasks data
      isLoading: false, // Show loading state
      errorMessage: '' // Error message if fetching fails
    };
  },
  methods: {
    // Fetch all tasks from the backend
    async fetchTasks() {
      this.isLoading = true; // Show loading state
      this.errorMessage = ''; // Clear any previous errors
      try {
        const response = await fetch("http://localhost:8000/tasks/");
        if (!response.ok) {
          throw new Error("Failed to fetch tasks");
        }
        const data = await response.json();
        this.tasks = data; // Update tasks list
      } catch (error) {
        console.error("Error fetching tasks:", error);
        this.errorMessage = "Failed to load tasks. Please try again later.";
      } finally {
        this.isLoading = false; // Hide loading state
      }
    },

    // Fetch tasks sorted by priority from the backend
    async fetchSortedTasks() {
      this.isLoading = true;
      this.errorMessage = '';
      try {
        const response = await fetch("http://localhost:8000/tasks/sorted");
        if (!response.ok) {
          throw new Error("Failed to fetch sorted tasks");
        }
        const data = await response.json();
        this.tasks = data; // Update with sorted tasks
      } catch (error) {
        console.error("Error fetching sorted tasks:", error);
        this.errorMessage = "Failed to load sorted tasks. Please try again later.";
      } finally {
        this.isLoading = false;
      }
    },

    // Delete task by id
    async deleteTask(taskId) {
      if (confirm("Are you sure you want to delete this task?")) {
        try {
          const response = await fetch(`http://localhost:8000/tasks/${taskId}`, {
            method: 'DELETE',
          });

          if (response.ok) {
            // Remove the task from the task list after successful deletion
            this.tasks = this.tasks.filter(task => task.id !== taskId);
            alert("Task deleted successfully");
          } else {
            alert("Failed to delete task");
          }
        } catch (error) {
          console.error("Error deleting task:", error);
        }
      }
    },

    // Redirect to task edit page or open modal for task editing
    editTask(task) {
      // Assuming you're using Vue Router, navigate to an edit page
      // where you will handle task update, or open a modal for inline edit
      this.$router.push({ name: 'EditTask', params: { id: task.id } });

      // Alternatively, you can open an inline form for editing directly in this component
      // using modal or inline edit.
    }
  },
  mounted() {
    // Fetch tasks when the component is mounted
    this.fetchTasks();
  }
};
</script>

<style scoped>
.list-group-item {
  margin-bottom: 10px;
  padding: 15px;
}
.badge {
  margin-top: 5px;
}
</style>
