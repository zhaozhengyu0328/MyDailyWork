import axios from 'axios'

const http = axios.create({
    //通用请求的地址前缀
    baseURL : '/api',
    timeout : 1000,
})
// Add a request interceptor
http.interceptors.request.use(function (config) {
  // Do something before request is sent
  return config;
}, function (error) {
  // Do something with request error
  return Promise.reject(error);
});

// Add a response interceptor
http.interceptors.response.use(function (response) {
  // Do something with response data
  return response;
}, function (error) {
  // Do something with response error
  return Promise.reject(error);
});

export default http
