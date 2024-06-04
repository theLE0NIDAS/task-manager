<template>
  <div class="task-form">
    <h3>Create a New Task</h3>
    <form @submit.prevent="createTask">
      <div class="mb-3">
        <label for="title" class="form-label">Task Title</label>
        <input
          type="text"
          id="title"
          v-model="task.title"
          class="form-control"
          placeholder="Enter task title"
          required
        />
      </div>
      <div class="mb-3">
        <label for="priority" class="form-label">Task Priority</label>
        <select id="priority" v-model="task.priority" class="form-select" required>
          <option value="" disabled>Select Priority</option>
          <option value="Very High">Very High</option>
          <option value="High">High</option>
          <option value="Moderate">Moderate</option>
          <option value="Low">Low</option>
          <option value="Very Low">Very Low</option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Add Task</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      task: {
        title: "",
        priority: ""
      }
    };
  },
  methods: {
    async createTask() {
      try {
        const response = await fetch("http://localhost:8000/tasks/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.task)
        });

        if (response.ok) {
          alert("Task created successfully!");
          this.task.title = "";
          this.task.priority = "";
          this.$emit("taskCreated"); // To trigger parent refresh
        } else {
          alert("Failed to create task.");
        }
      } catch (error) {
        console.error("Error creating task:", error);
      }
    }
  }
};
</script>

<style scoped>
.task-form {
  max-width: 500px;
  margin: 20px auto;
}
</style>
