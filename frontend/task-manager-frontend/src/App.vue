<!--
<template>
  <div class="container">
    <h1>Task Manager</h1>
    <task-form @taskCreated="fetchTasks" />
    <task-list ref="taskList" />
  </div>
</template>

<script>
import TaskForm from "./components/TaskForm.vue";
import TaskList from "./components/TaskList.vue";

export default {
  components: {
    TaskForm,
    TaskList
  },
  methods: {
    fetchTasks() {
      this.$refs.taskList.fetchTasks();
    }
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
}
</style>
-->


<template>
  <div class="container">
    <nav>
      <RouterLink to="/">Task Manager</RouterLink > |
      <RouterLink to="/dependent-tasks">Manage Dependent Tasks</RouterLink >
    </nav>
    <RouterView />
  </div>
</template>

<script>
export default {
  components: {
    // No need to directly import components here since we're using router-view
  },
};
</script>

<style scoped>
.container {
  padding: 20px;
}

nav {
  margin-bottom: 20px;
}

nav a {
  margin-right: 10px;
  text-decoration: none;
  color: #007bff;
}

nav a:hover {
  text-decoration: underline;
}
</style>