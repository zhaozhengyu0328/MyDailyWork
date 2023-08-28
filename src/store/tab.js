export default {
    state: {
        isCollapse: false,  // 用于控制菜单的展开还是收起
        tabsList: [
            {
                path: "/",
                name: "home",
                label: "首页",
                icon: "s-home",
                url: "Home/Home",
            }
        ] // 面包屑的数据
    },
    mutations:
    // 修改菜单展开收起的方法
    {
        collapseMenu(state) {
            state.isCollapse = !state.isCollapse
        },
        // 更新面包屑数据
        selectMenu(state, val) {
            console.log(val, 'val')
            // 判断添加的数据是否为首页
            if (val.name !== 'home') {
                const index = state.tabsList.findIndex(item => item.name === val.name)
                // 如果不存在
                if (index === -1) {
                    state.tabsList.push(val)
                }
            }
        },
        // 这个mutation是用来删除指定的tag数据
        closeTag(state, item){
            console.log(item, 'item')
            const index = state.tabsList.findIndex(val => val.name === item.name)  //如果我们传入的name和现有的tableList里面的名字重叠,那么就返回这个name
            state.tabsList.splice(index, 1)
        }
    },
    getter:{

    },
    action:{
        
    }
}