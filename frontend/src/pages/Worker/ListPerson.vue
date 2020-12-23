<template>
  <div class="row">
    <div class="col-md-12">
      <card>
        <b-table :items="model" :fields="fields">
        </b-table>
      </card>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
  export default {
    props: {
      model: {
        type: Array,
        default: () => {
          return {};
        }
      }
    },
    data() {
      return {
        items: [],
        fields: [
          { key: 'time', label: '시간'},
          { key: 'action', label: '상태'}
        ],
      }
    },
    methods : {
    },
    mounted() {
    }
  }
</script>
<style>
option {
  color : rgb(0, 0, 0)
}
</style>