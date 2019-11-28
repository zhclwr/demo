<template>
	<el-table-column
            :width="column.width"
            :prop='column.key'
            :align='column.align'
            :label="column.title">
        <template slot-scope="scope">
            <expand
                    v-if="column.render"
                    :render="column.render"
                    :index="scope.index"
                    :row="scope.row"
                    :column="column">
            </expand>
            <span v-else>{{scope[scope.row.key]}}</span>
        </template>
		<columnD v-for="(column, childIndex) in column.children" :key="childIndex" :column="column"></columnD>
	</el-table-column>
</template>

<script>
    import expand from './expand.vue'
    export default {
        name: 'columnD',
        props: {
            column:{ required: true}
        },
        components: {expand}
    }
</script>

<style>

</style>