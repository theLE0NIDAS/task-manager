<template>
  <div>
    <h1>Task Manager</h1>

    <!-- Display message for feedback or errors -->
    <p v-if="message">{{ message }}</p>

    <!-- Button to refresh the task list -->
    <button @click="fetchTasks" class="btn btn-primary mb-3">Fetch Tasks</button>

    <!-- Display tasks in a table -->
    <table v-if="tasks.length > 0" class="table table-bordered">
      <thead>
        <tr>
          <th>Title</th>
          <th>Priority</th>
          <th>Description</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in tasks" :key="task.id">
          <td>{{ task.title }}</td>
          <td>{{ task.priority }}</td>
          <td>{{ task.description }}</td>
          <td>{{ task.status }}</td>
        </tr>
      </tbody>
    </table>

    <!-- No tasks message -->
    <p v-else>No tasks available. Please add a task.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tasks: [], // Stores the list of tasks fetched from the backend
      message: '', // Feedback message
    };
  },
  methods: {
    // Fetch all tasks from the backend
    async fetchTasks() {
      try {
        const response = await fetch('http://127.0.0.1:8000/tasks/');
        if (!response.ok) {
          throw new Error('Failed to fetch tasks');
        }
        const data = await response.json();
        this.tasks = data; // Set the tasks to the response data
        this.message = ''; // Clear any previous error messages
      } catch (error) {
        console.error('Error fetching tasks:', error);
        this.message = 'Failed to fetch tasks from the backend.';
      }
    },
  },
  mounted() {
    // Fetch tasks when the component is mounted
    this.fetchTasks();
  },
};
</script>

<style scoped>
h1 {
  color: #2c3e50;
  font-size: 24px;
}
.table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
}
.table th, .table td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: left;
}
.table th {
  background-color: #f4f4f4;
}
</style>
