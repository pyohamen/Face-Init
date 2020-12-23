<template>
    <div>
      <div class="row">
        <div class="col-12 text-center">
          <h1 v-text="currentTime"></h1>
        </div>
      </div>
      <div class="row">
        <div class="col-12 text-center">
          <card>
            <h2>최근 태그된 사원</h2>
            <div class="row">
              <div class="col-6 text-center" style="margin-top: auto; margin-bottom: auto;">
                <h3 class="align-middle">{{ people[0].department }} | {{ people[0].kor_name }} | {{ people[0].position }} | {{ people[0].time }}</h3>
              </div>
              <div class="col-6">
                <b-img style="max-height: 350px" :src="require(`@/assets/images/people/${people[0].id}.jpg`)"  fluid />
              </div>
            </div>
          </card>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-6 col-md-12 text-center">
          <card>
            <h5 slot="header" class="title">카메라</h5>
            <img class="img-fluid" style="-webkit-user-select: none;margin: auto;" src="http://ssafyteam7.iptime.org:8080/video_feed" @error="$event.target.src=require(`@/assets/images/alt_camera.jpg`)"/>
          </card>
        </div>
        <div class="col-lg-6 col-md-12 text-center">
          <card>
            <b-table
              small
              id="my-table"
              :items="people"
              :fields="fields"
              ref="table"
            >
              <template v-slot:row-details="row">
                <b-card>
                  <ul>
                    <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                  </ul>
                </b-card>
              </template>
            </b-table>
          </card>
        </div>
      </div>
      <!-- 확인 메시지 -->
      <modal :show.sync="modal"
              body-classes="p-0"
              modal-classes="modal-sm">
        <h3 slot="header" class="modal-title" id="modal-title-default" style="color: rgba(255,255,255,0.8)">알람</h3>
        <hr/>
        <h4 class="text-center" style="color: rgba(255,255,255,0.8)"> 인식이 되지 않는 사원입니다. </h4>
        <template slot="footer">
          <base-button type="secondary" class="ml-auto" @click="closeModal()">확인</base-button>
        </template>
      </modal>
    </div>
</template>
<script>
/* eslint-disable */
  import altImage from '@/assets/images/alt_camera.jpg'
  import {Modal} from '@/components'
  import axios from 'axios'

  export default {
    data() {
        return {
            currentTime: null,
            altCamera : altImage,
            people : [
              {
                id : 0,
                department : '',
                kor_name : '',
                position : '',
                time : '',
              }
            ],
            fields: [
                { key: 'kor_name', label: '이름' },
                { key: 'department', label: '부서' },
                { key: 'position', label: '직책' },
                { key: 'time', label: '시간' }
            ],
            isModal : false,
            modal : false,
        }
    },
    components: {
        Modal,
    },
    methods: {
      updateCurrentTime () {
        this.currentTime = this.$moment().format().substring(0, 10) + ' '  + this.$moment().format('LTS')
        this.loadPk()
        this.onUpdate()
      },
      loadPk(){
        axios.get(`http://i3a207.p.ssafy.io:8000/blog/api/v1/`)
          .then(({ data }) => {
            this.tempData = data
          })
          .then(() => {
            for(let i = 0 ; i < this.tempData.length; i++){
              axios.get(`http://i3a207.p.ssafy.io:8000/blog/api/group/${this.tempData[i].user_pk}`)
                .then(({data}) => {
                  // null 인 경우
                  if(data.id == 37){
                    if(i == 0 && !this.isModal){
                      this.isModal = true
                      this.modal = true
                    }
                    this.people[i].id = data.id
                    this.people[i].kor_name = '이름없음'
                    this.people[i].department = '알수없음'
                    this.people[i].position = '알수없음'
                    this.people[i].time = this.tempData[i].recent.substring(11, 19)
                  }
                  else{
                    if(i == 0){
                      this.isModal = false
                    }
                    this.people[i] = data
                    this.people[i].time = this.tempData[i].recent.substring(11, 19)
                  }
              })
            }
          })
      },
      onUpdate() {
        this.$refs.table.refresh()
      },
      closeModal() {
        this.modal = false
      }
    },
    created(){
    },
    mounted (){
      this.currentTime = this.$moment().format().substring(0, 10) + ' '  + this.$moment().format('LTS')
      setInterval(() => this.updateCurrentTime(), 1 * 1000)
    }
  }
</script>
<style>
</style>