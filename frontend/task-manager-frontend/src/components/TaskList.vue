<template>
  <div>
    <h3>Task List</h3>
    <button @click="fetchSortedTasks" class="btn btn-secondary mb-3">Sort by Priority</button>
    <ul class="list-group">
      <li v-for="task in tasks" :key="task.id" class="list-group-item">
        <strong>{{ task.title }}</strong> - {{ task.priority }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tasks: []
    };
  },
  methods: {
    async fetchTasks() {
      try {
        const response = await fetch("http://localhost:8000/tasks/");
        const data = await response.json();
        this.tasks = data;
      } catch (error) {
        console.error("Error fetching tasks:", error);
      }
    },
    async fetchSortedTasks() {
      try {
        const response = await fetch("http://localhost:8000/tasks/sorted");
        const data = await response.json();
        this.tasks = data;
      } catch (error) {
        console.error("Error fetching sorted tasks:", error);
      }
    }
  },
  mounted() {
    this.fetchTasks();
  }
};
</script>
