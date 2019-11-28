<template>
	<div id="app">
		<el-table :data="tableData" style="width: 50%;margin:0 auto;">
			<el-table-column prop="date" label="日期" width="180"></el-table-column>
			<el-table-column prop="name" label="姓名" width="180"></el-table-column>
			<el-table-column prop="address" label="地址"></el-table-column>
		</el-table>
		<my-table :columns="columns" :tableData="tableData"></my-table>
	</div>
</template>

<script lang="ts">
    import {Component, Vue} from "vue-property-decorator";
    import HelloWorld from "./components/HelloWorld.vue";
    import MyTable from "./components/my-table.vue";

    @Component({
        components: {
            HelloWorld, MyTable
        },
        data() {
            return {
                tableData: [
                    {
                        date: "2016-05-02",
                        name: "王小虎",
                        address: "上海市普陀区金沙江路 1518 弄"
                    },
                    {
                        date: "2016-05-04",
                        name: "王小虎",
                        address: "上海市普陀区金沙江路 1517 弄"
                    },
                    {
                        date: "2016-05-01",
                        name: "王小虎",
                        address: "上海市普陀区金沙江路 1519 弄"
                    },
                    {
                        date: "2016-05-03",
                        name: "王小虎",
                        address: "上海市普陀区金沙江路 1516 弄"
                    }
                ],
                columns: [
                    {
                        title: "日期",
                        key: 'date'
                    },
                    {
                        title: "配送信息",
                        children: [
                            {
                                title: "姓名",
                                key: 'name'
                            },
                            {
                                title: "年龄",
                                key: 'age'
                            },
                        ]
                    }
                ]
            };
        }
    })
    export default class App extends Vue {
    }
</script>

<style>
	#app {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		margin-top: 60px;
	}
</style>
