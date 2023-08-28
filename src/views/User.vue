<template>
  <div class="manage">
    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="50%"
      :before-close="handleClose"
    >
      <!-- 用户的表单信息 -->
      <el-form ref="form" :rules="rules" :model="form" label-width="80px">
        <el-form-item label="姓名" prop="name">
          <el-input playcehoder="请输入姓名" v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="年龄" prop="age">
          <el-input playcehoder="请输入年龄" v-model="form.age"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-select v-model="form.sex" placeholder="请选择性别">
            <el-option label="男" :value="1"></el-option>
            <!-- lable显示文案，value表示传的真实值 -->
            <el-option label="女" :value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="生日" prop="birth">
          <el-col :span="11">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="form.birth"
              value-format="yyyy-MM-dd"
            ></el-date-picker>
          </el-col>
        </el-form-item>
        <el-form-item label="地址" prop="addr">
          <el-input playcehoder="请输入地址" v-model="form.addr"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancel">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </span>
    </el-dialog>
    <div class="manage-header">
      <el-button @click="handleAdd" type="primary" class='create_button'> + 新增 </el-button>
      <!-- form搜索区域 -->
      <el-form :inline=true :model="userform">
          <el-form-item>
              <el-input playcehoder="请输入名称" v-model="userform.name"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type='primary' @click="onSubmit"> 查询</el-button>
          </el-form-item>
      </el-form>
    </div>
    <!-- 下半部分表单展示 -->
    <div class="common-table">
      <el-table :data="tableData" style="width: 100% height:90%" stripe>
        <el-table-column prop="name" label="姓名"> </el-table-column>
        <el-table-column prop="sex" label="性别">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{
              scope.row.sex == 1 ? "男" : "女"
            }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="age" label="年龄"> </el-table-column>
        <el-table-column prop="birth" label="出生日期"> </el-table-column>
        <el-table-column prop="addr" label="地址"> </el-table-column>
        <el-table-column prop="addr" label="地址">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.row)"
              >编辑</el-button
            >
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.row)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页 -->
    </div>
    <div>
        <el-pagination
          layout="prev, pager, next"
          :total="total"
          @current-change="handlePage"
          class = pager
        >
        </el-pagination>
      </div>
  </div>
</template>
<script>
import { addUser, delUser, editUser, getUser } from "../api";
export default {
  data() {
    return {
      dialogVisible: false,
      form: {
        name: "",
        age: "",
        sex: "",
        birth: "",
        addr: "",
      },
      rules: {
        name: [{ required: true, message: "请输入姓名" }],
        age: [{ required: true, message: "请填写年龄" }],
        sex: [{ required: true, message: "请至少选择一个性别" }],
        birth: [{ required: true, message: "请选择日期" }],
        addr: [{ required: true, message: "请填写地址" }],
      },
      tableData: [],
      modalType: 0, //0 表示新增弹窗， 1 表示编辑弹窗
      total: 0, // 当前的总条数默认为零
      pageData: {
        page: 1,
        limit: 10,
      },
      userform: {
          name: ''
      }
    };
  },
  methods: {
    //提交用户表单
    submit() {
      this.$refs.form.validate((valid) => {
        // console.log(valid,'valid')
        if (valid) {
          // 如果校验通过，那么后台就可以拿到数据了

          if (this.modalType === 0) {
            addUser(this.form).then(() => {
              this.getList();
            });
          } else {
            editUser(this.form).then(() => {
              this.getList();
            });
          }
          // console.log(this.form, "form");
          // 清空表单
          this.$refs.form.resetFields();
          // 关闭弹窗
          this.dialogVisible = false;
        }
      });
    },
    handleClose() {
      this.$refs.form.resetFields();
      this.dialogVisible = false;
    },
    cancel() {
      this.handleClose();
    },
    handleEdit(row) {
      this.modalType = 1;
      this.dialogVisible = true;
      // 需要对当前行数据进行深拷贝
      this.form = JSON.parse(JSON.stringify(row));
    },
    handleDelete(row) {
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          delUser({ id: row.id }).then(() => {
            this.$message({
              type: "success",
              message: "删除成功!",
            });
            this.getList();
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
    handleAdd() {
      this.modalType = 0;
      this.dialogVisible = true;
      this.$refs.form.resetFields();
    },
    getList() {
      getUser({ params: {...this.userform, ...this.pageData } }).then(({ data }) => {
        console.log(data);
        this.tableData = data.list;
        this.total = data.count || 0;
      });
    },
    // 选择页码的回调函数
    handlePage(val) {
      console.log(val, "val");
      this.pageData.page = val;
      this.getList();
    },
    //列表查询
    onSubmit(){
        this.getList()
    }
  },
  mounted() {
    this.getList();
  },
};
</script>
<style lang="less">
.manage {
  height: 80%;
  position: relative;
  .manage-header {
    display: flex;
    justify-content: space-between;
    align-content: center;
    .create_button{
      // padding:10px
      margin-bottom: 22px;
      // border:none
    }
  }
  .common-table{   
      position: relative;
      height: 90%;
  }
  .pager{
      position: absolute;
      bottom: 0;
      right: 20px;
    }
}
</style>