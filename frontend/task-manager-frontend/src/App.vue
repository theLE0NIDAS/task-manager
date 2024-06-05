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
