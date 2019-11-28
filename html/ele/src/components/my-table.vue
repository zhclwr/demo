<template>
    <el-table :data="tableData">
        <column v-for="(column, index) in columns" :column="column" :key="index"></column>
    </el-table>
</template>
<script lang="ts">
import { Component, Vue,Inject, Prop, Watch } from 'vue-property-decorator';
import expand from './expand.vue'
import column from './column.vue'

@Component({
  components:{expand,column}
})
export default class extends Vue{
    @Prop({type:Array}) tableData:Array<any>;
    @Prop({type:Array}) columns:Array<any>;
    @Prop({type:Number}) currentPage:Number;
    @Prop({type:Number}) total:Number;
    @Prop({type:Number}) height:Number;
    @Prop({type:Boolean,default:false}) notPagination:Boolean;
    @Prop({type:Boolean,default:false}) loading:Boolean;
    @Prop({type:Boolean,default:false}) showSummary:Boolean;
    @Prop({type:Boolean,default:false}) indexHidden:Boolean;
    @Prop({type:String,default:'mytable'}) id:String;
    @Prop({type:Boolean,default:false}) isSelection:Boolean;
    @Prop({type:Function,}) rowClassName:Function;

    handleCurrentChange(val:any){
      this.$emit('handleCurrentChange',val)
    }
    handleSizeChange(val:any){
      this.$emit('handleSizeChange',val)
    }
}
</script>