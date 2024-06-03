<template>
  <div>
    <h1>Task Manager</h1>
    <p>{{ message }}</p>
    <button @click="fetchMessage">Fetch from FastAPI</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
    };
  },
  methods: {
    async fetchMessage() {
      try {
        const response = await this.$http.get('http://127.0.0.1:8000/');
        this.message = response.data.message;
      } catch (error) {
        console.error('Error fetching message:', error);
        this.message = 'Failed to fetch data from the backend';
      }
    },
  },
};
</script>

<style scoped>
h1 {
  color: #2c3e50;
  font-size: 24px;
}
</style>
