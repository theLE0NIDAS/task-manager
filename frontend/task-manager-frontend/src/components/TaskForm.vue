<template>
  <div class="task-form">
    <h3>Create a New Task</h3>
    <form @submit.prevent="createTask">
      <!-- Task Title -->
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

      <!-- Task Priority -->
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

      <!-- Task Description -->
      <div class="mb-3">
        <label for="description" class="form-label">Task Description</label>
        <input
          type="text"
          id="description"
          v-model="task.description"
          class="form-control"
          placeholder="Enter task description"
        />
      </div>

      <!-- Task Status -->
      <div class="mb-3">
        <label for="status" class="form-label">Task Status</label>
        <select id="status" v-model="task.status" class="form-select" required>
          <option value="" disabled>Select Status</option>
          <option value="Pending">Pending</option>
          <option value="In Progress">In Progress</option>
          <option value="Completed">Completed</option>
        </select>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn btn-primary">Add Task</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      task: {
        title: "",         // Task title
        priority: "",      // Task priority
        description: "",   // Task description
        status: "Pending"  // Default to 'Pending' status
      }
    };
  },
  methods: {
    async createTask() {
      try {
        const response = await fetch("http://localhost:8000/tasks/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.task),
        });

        if (response.ok) {
          alert("Task created successfully!");
          this.resetForm();
          this.$emit("taskCreated"); // To notify parent component
        } else {
          alert("Failed to create task.");
        }
      } catch (error) {
        console.error("Error creating task:", error);
      }
    },
    resetForm() {
      this.task.title = "";
      this.task.priority = "";
      this.task.description = "";
      this.task.status = "Pending";  // Reset to default status
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
