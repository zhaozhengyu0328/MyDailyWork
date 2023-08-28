<template>
    <div class="tabs">
        <el-tag          
            v-for="(item, index) in tags"
            :key="item.path"
            :closable="item.name !== 'home'"            
            :effect="$route.name === item.name ? 'dark' : 'plain'"
            @click="changeMenu(item)"
            @close="handleClose(item, index)">
            {{ item.label }}
        </el-tag>
        <!-- closable：若不是首页，可进行关闭  effect：判断是不是最新的一个，然后高亮-->
    </div>
</template>
<script>
import { mapState, mapMutations } from 'vuex'
export default {
    name:'CommonTag',
    data() {
        return {}
    },
    computed:{
        ...mapState({
            tags:state => state.tab.tabsList
        })
    },
    methods:{
        ...mapMutations(['closeTag']),
        // 点击tag跳转的功能
        changeMenu(item){
            // console.log(item)
            this.$router.push({ name:item.name })
        },
        // 删除tag功能   逻辑上会难一点
        handleClose(item, index){
            // 调用store中的mutation
            // this.$store.commit('closeTag')                      // 使用commit方法也可以,教程里面使用的是辅助函数
            this.closeTag(item)
            const length = this.tags.length
            // 删除之后的跳转逻辑
            if (item.name !== this.$route.name){
                return          
            }
            // 表示删除最后一项
            if (index === length){
                 this.$router.push({
                        name: this.tags[index - 1].name
                 })
            } else{
                this.$router.push({
                        name: this.tags[index].name
                })
            }
            // 如果删除的是
        }
    }
}
</script>
<style scoped>
    .el-tag{
        margin-top: 10px;
        margin-left: 20px;
    }
</style>