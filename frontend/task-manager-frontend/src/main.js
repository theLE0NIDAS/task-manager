import './assets/main.css'

import 'bootstrap/dist/css/bootstrap.css'
import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router';

const app = createApp(App);

// Set axios globally
app.config.globalProperties.$http = axios;

// app.mount('#app');
createApp(App).use(router).mount('#app');
