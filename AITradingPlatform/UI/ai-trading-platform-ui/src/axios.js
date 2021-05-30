import axios from 'axios'

axios.defaults.baseURL='http://localhost:1300';
axios.defaults.headers.common["Autherization"]='Bearer' + localStorage.getItem('token');