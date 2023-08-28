<template>
  <div class="header-container">
    <div class="l-content">
      <el-button
        @click="handleMenu"
        icon="el-icon-menu"
        size="mini"
      ></el-button>
      <!-- size 控制大小 -->
      <!-- 面包屑 -->
      <el-breadcrumb separator="/" style="margin-left:20px">
        <el-breadcrumb-item v-for="item in tags" :key="item.path"  :to="{ path: item.path }">{{ item.label }}</el-breadcrumb-item>   <!-- 这里的动态数据如何使用呢？    1. this.$store.state具体模块获取内容  2. 使用辅助函数(教程所用) -->
      </el-breadcrumb>
    </div>
    <div class="r-content">
      <el-dropdown>
        <span class="el-dropdown-link">
          <img class="user" src="../imgs/叙利亚战斗.jpg" alt="" />
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>个人中心</el-dropdown-item>
          <el-dropdown-item>退出</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>
<script>
// <!-- 这里的动态数据如何使用呢？    1. this.$store.state具体模块获取内容  2. 使用辅助函数(教程所用) -->
import { mapState } from 'vuex'
export default {
  data() {
    return {};
  },
  methods: {
    handleMenu() {
      this.$store.commit("collapseMenu");
    },
  },
  computed:{
      ...mapState({                             //... 是ES6的对象结构方法
        tags : (state) => {return state.tab.tabsList}
      })
  },
  mounted(){
    console.log(this.tags, 'tags')
  }
};
</script>
<style lang ="less" scoped>
.header-container {
  padding: 0 20px;
  background-color: #333;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;

  .text {
    color: #fff;
    font-size: 14px;
    margin-left: 10px;
  }
  .r-content {
    .user {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      margin-right: 15px;
    }
  }
  .l-content {
        display: flex;
        align-items: center;
        /deep/.el-breadcrumb__item{
            .el-breadcrumb__inner {
                font-weight:normal;
                &.is-link {
                    color:#666
                }
            }
            &:last-child {
                .el-breadcrumb__inner{
                    color: #fff;
                }
            }
        }
    }
}
</style>