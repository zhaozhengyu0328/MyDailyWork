import http from'../utils/request'

// 请求数据接口（首页数据）

export const getData = () => {
    // 返回一个promise对象
    return http.get('/home/getData')
}

export const getUser = (params) => {
    // 返回用户列表
    return http.get('/user/getUser', params )
}
// 在axios中, post方法返回的是data.
export const addUser = (data) =>{
    return http.post('/user/add', data )
}

export const editUser = (data) =>{
    return http.post('/user/edit', data )
}

export const delUser = (data) =>{
    return http.post('/user/del', data )
}