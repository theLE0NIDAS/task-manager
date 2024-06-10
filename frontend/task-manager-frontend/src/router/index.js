// src/router/index.js
import { createRouter, createMemoryHistory } from 'vue-router';
import TaskManager from '@/components/TaskManager.vue';  // Your main task manager page
import TaskFormWithDependencies from '@/components/TaskFormTopo.vue'; // The new component

const routes = [
  {
    path: '/',
    name: 'TaskManager',
    component: TaskManager
  },
  {
    path: '/dependent-tasks',
    name: 'DependentTasks',
    component: TaskFormWithDependencies
  }
];

const router = createRouter({
  history: createMemoryHistory(),
  routes
});

export default router;
