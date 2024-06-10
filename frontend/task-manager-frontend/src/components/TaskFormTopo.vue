<template>
  <h1>Task Manager</h1>
  <div class="task-form">
    <h3>Create a New Dependent Task</h3>
    <form @submit.prevent="createDependentTask">
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
      <div class="mb-3">
        <label for="depends_on" class="form-label">Task Dependencies (IDs of other tasks)</label>
        <input
          type="text"
          id="depends_on"
          v-model="task.depends_on"
          class="form-control"
          placeholder="Enter task IDs this task depends on, comma-separated"
        />
      </div>
      <button type="submit" class="btn btn-primary">Add Dependent Task</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      task: {
        title: "",
        priority: "",
        description: "",
        status: "",
        depends_on: ""
      }
    };
  },
  methods: {
    async createDependentTask() {
      try {
        const response = await fetch("http://localhost:8000/tasks/dependent", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            ...this.task,
            depends_on: this.task.depends_on.split(",").map(dep => dep.trim())
          })
        });

        if (response.ok) {
          alert("Dependent task created successfully!");
          this.$emit("taskCreated");
        } else {
          alert("Failed to create dependent task.");
        }
      } catch (error) {
        console.error("Error creating dependent task:", error);
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
