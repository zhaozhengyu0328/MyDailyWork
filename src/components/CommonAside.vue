<template>
  <el-menu
    default-active="1-4-1"
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
    :collapse="isCollapse"
  >
    <h3>{{  isCollapse ? '后台':'通用后台管理系统' }}</h3>

    <el-menu-item
      @click="clickMenu(item)"
      v-for="item in noChildren"
      :key="item.name"
      :index="item.name"
    >
      <i :class="`el-icon-${item.icon}`"></i>
      <!-- 变为动态class，并使用ES6的模板字符串语法 ，此非单引号其实为~的小写形式 -->
      <span slot="title">{{ item.label }}</span>
    </el-menu-item>

    <el-submenu
      v-for="item in hasChildren"
      :key="item.label"
      :index="item.label"
    >
      <template slot="title">
        <i :class="`el-icon-${item.icon}`"></i>
        <span slot="title">{{ item.label }}</span>
      </template>

      <el-menu-item-group
        
        v-for="subItem in item.children"
        :key="subItem.path"
        :index="subItem.path"
      >
        <el-menu-item  @click="clickMenu(subItem)" :index="subItem.path">{{
          subItem.label
        }}</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
  </el-menu>
</template>

<style lang = 'less' scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.el-menu {
  height: 100vh;
  background-color: rgb(211, 204, 204);
  h3 {
    color: black;
    text-align: center;
    line-height: 48px;
    font-style: 16px;
    font-weight: 400px;
  }
}
</style>

<script>
export default {
  data() {
    return {
      
      menuData: [
        {
          path: "/",
          name: "home",
          label: "首页",
          icon: "s-home",
          ur1: "Home/Home",
        },
        {
          path: "/mall",
          name: "mall",
          label: "商品管理",
          icon: "video-play",
          url: "MallManage/MallManage",
        },
        {
          path: "/user",
          name: "user",
          label: "用户管理",
          icon: "user",
          url: "UserManage/UserManage",
        },
        {
          label: "其他",
          icon: "location",
          children: [
            {
              path: "/page1",
              name: "page1",
              label: "页面1",
              icon: "setting",
              url: "other/PageOne",
            },
            {
              path: "/page2",
              name: " page2",
              label: "页面2",
              icon: "setting",
              ur1: "other/PageTwo",
            },
          ],
        },
      ],
    };
  },

  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    //点击菜单
    clickMenu(item) {
      console.log(item);
      // 解决当页面的路由和跳转的路由不一致才允许跳转
      if (this.$route.path !== item.path && !(this.$router.path === '/home' && (item.path === '/'))){
          this.$router.push(item.path);
      }
      this.$store.commit('selectMenu', item)   // 在这里可以获取route内容， 然后通过 sotre的 commit方法提交给后台处理
    }
  },
  computed: {
    // 没有子菜单
    noChildren() {
      return this.menuData.filter((item) => !item.children);
    },
    // 有子菜单
    hasChildren() {
      return this.menuData.filter((item) => item.children);
    },
    isCollapse(){
      return this.$store.state.tab.isCollapse
    }
  },
};
</script>
<style scoped>
.el-menu{
  border-right: 0px;
}
</style>
