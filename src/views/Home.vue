<template>
  <el-row>
    <el-col :span="8" style="padding: 10px">
      <el-card class="box-card">
        <div class="user">
          <img src="../imgs/叙利亚战斗.jpg" alt="" />
          <div div class="userinfo">
            <p class="name">Admin</p>
            <p class="access">超级管理员</p>
          </div>
        </div>
        <div class="login-info">
          <p>上次登陆时间<span>2023-3-12</span></p>
          <p>上次登陆地点<span>武汉</span></p>
        </div>
      </el-card>
      <el-card style="height: 460px">
        <el-table :data="tableData" style="width: 100%">
          <el-table-column
            v-for="(val, key) in tableLabel"
            :prop="key"
            :label="val"
            :key="key"
          />
        </el-table>
        <!-- <el-table-column
                prop="date"
                label="日期">
              </el-table-column>
              <el-table-column
                prop="name"
                label="姓名">
              </el-table-column>
              <el-table-column
                prop="address"
                label="地址">
              </el-table-column>  
              <el-table-column
                prop="good"
                label="货物">
              </el-table-column>  太过于繁琐-->
      </el-card>
    </el-col>
    <el-col :span="16" style="padding: 10px">
      <div class="grid-content bg-purple-light"></div>
      <div class="num">
        <el-card
          v-for="item in countData"
          :key="item.name"
          :body-style="{ display: 'flex', padding: 0 }"
        >
          <i
            class="icon"
            :class="`el-icon-${item.icon}`"
            :style="{ background: item.color }"
          ></i>
          <div class="detail">
            <p class="price">¥ {{ item.value }}</p>
            <p class="desc">{{ item.name }}</p>
          </div>
        </el-card>
      </div>
      <el-card style="height: 280px">
        <!-- 折线图 -->
        <div ref="echarts1" style="height: 280px"></div>
      </el-card>
      <div class="graph">
        <!-- 柱状图 -->
        <el-card>
          <div ref="echarts2" style="height: 260px"></div>
        </el-card>
        <el-card>
          <!-- 趋势图 -->
          <div ref="echarts3" style="height: 240px"></div>
        </el-card>
      </div>
    </el-col>
  </el-row>
</template>
<script>
import { getData } from "../api";
import * as echarts from "echarts";
import { Axios } from "axios";
export default {
  data() {
    return {
      tableData: [],
      tableLabel: {
        name: "课程",
        todayBuy: "今日购买",
        monthBuy: "本月购买",
        totalBuy: "总购买",
      },
      countData: [
        {
          name: "今日支付订单",
          value: "40",
          icon: "success",
          color: "#2ec7c9",
        },
        {
          name: "支付订单",
          value: "40",
          icon: "success",
          color: "#2ec7c9",
        },
        {
          name: "今日订单",
          value: "40",
          icon: "success",
          color: "#2ec7c9",
        },
        {
          name: "今付订单",
          value: "40",
          icon: "success",
          color: "#2ec7c9",
        },
        {
          name: "今日支订单",
          value: "40",
          icon: "success",
          color: "#2ec7c9",
        },
        {
          name: "今日单",
          value: "40",
          icon: "success",
          color: "#2ec7c9",
        },
      ],
    };
  },
  mounted() {
    getData().then(({ data }) => {
      const { tableData } = data.data;
      this.tableData = tableData;
      // 基于准备好的dom，初始化echarts实例
      const echarts1 = echarts.init(this.$refs.echarts1);
      // 指定图表的配置项和数据
      var echarts1Option = {};
      //处理数据xAxis
      const { orderData, userData, videoData } = data.data;
      const xAxis = Object.keys(orderData.data[0]);
      // console.log(xAxis);
      const legend = orderData.date;
      // console.log(legend);
      const legendData = {
        data: legend,
      };
      const xAxisData = {
        data: xAxis,
      };
      // console.log(xAxis)
      echarts1Option.xAxis = legendData;
      echarts1Option.yAxis = {};
      echarts1Option.legend = xAxisData;
      echarts1Option.series = [];
      xAxis.forEach((key) => {
        //forEach: 遍历与循环，默认有三个传参：遍历的数组内容(item)、索引(index)、当前遍历(Array)
          echarts1Option.series.push({
          //map：基本与forEach一致，不同的是它会返回一个新数组，callback需有return值，如没有，会返回undefined
          name: key,
          data: orderData.data.map((item) => item[key]),
          // data: orderData.data.map(function(item){return item[key]}),    //https://blog.csdn.net/Maisuluo/article/details/128074645 理解JS中的map的多种用法
          type: "line", //方法定义在JavaScript的Array中，它返回一个新的数组，数组中的元素为原始数组调用函数处理后的值。
          // 值得注意的是：1、map()函数不会对空数组进行检测；2、map()函数不会改变原始数组，它形成的是 一个新的数组
        });
        });
        console.log(echarts1Option);
        // 使用刚指定的配置项和数据显示图表。
        echarts1.setOption(echarts1Option);
        
        // 柱状图
        const echarts2 = echarts.init(this.$refs.echarts2);
        // 指定图表的配置项和数据
        const echarts2Option = {
          legend: {
            // 图例文字颜色
            textStyle: {
              color: "#333",
            },
          },
          grid: {
            left: "20%",
          },
          // 提示框
          tooltip: {
            trigger: "axis",
          },
          xAxis: {
            type: "category", // 类目轴
            data: userData.map((item) => item.date),
            axisLine: {
              lineStyle: {
                color: "#17b3a3",
              },
            },
            axisLabel: {
              interval: 0,
              color: "#333",
            },
          },
          yAxis: [
            {
              type: "value",
              axisLine: {
                lineStyle: {
                  color: "#17b3a3",
                },
              },
            },
          ],
          color: ["#2ec7c9", "#b6a2de"],
          series: [
            {
              name: "新增用户",
              data: userData.map((item) => item.new),
              type: "bar",
            },
            {
              name: "活跃用户",
              data: userData.map((item) => item.active),
              type: "bar",
            },
          ],
        };
        echarts2.setOption(echarts2Option);
      
        // 饼状图
        const echarts3 = echarts.init(this.$refs.echarts3);
        // 指定图表的配置项和数据
        const echarts3Option = {
          tooltip: {
            trigger: "item",
          },
          color: [
            "#0f78f4",
            "#dd536b",
            "#9462e5",
            "#a6a6a6",
            "#e1bb22",
            "#39c362",
            "#3ed1cf",
          ],
          series: [
            {
              data: videoData,
              type: "pie",
            },
          ],
        };
        echarts3.setOption(echarts3Option);
    });
  },
};
</script>
<style lang="less" scoped>
.user {
  padding-bottom: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  display: flex;
  align-items: center;
  img {
    margin-right: 40px;
    width: 150px;
    height: 150px;
    border-radius: 50%;
  }
  .userinfo {
    .name {
      font-size: 32px;
      margin-bottom: 10px;
    }
    .access {
      color: #999999;
    }
  }
}
.login-info {
  p {
    line-height: 28px;
    font-size: 14px;
    color: #999999;
    span {
      color: #666666;
      margin-left: 60px;
    }
  }
}
.box-card {
  margin-bottom: 20px;
}
.num {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between; // flex贴边设置
  // margin-left: 20px;
  .icon {
    width: 80px;
    height: 80px;
    font-size: 30px;
    text-align: center;
    line-height: 80px;
    columns: #fff;
  }
  .detail {
    margin-left: 15px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    .price {
      font-size: 30px;
      margin-bottom: 10px;
      line-height: 30px;
      height: 30px;
    }
    .desc {
      font-size: 14px;
      color: #999;
      text-align: center;
    }
  }
  .el-card {
    width: 32%;
    margin-bottom: 20px;
  }
}
.graph {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
  height: 260px;
  .el-card {
    width: 48%;
  }
}
</style>