<template>
  <card title="사원 정보" >
    <b-col class="my-1 col-12">
      <b-form-group
        label="검색"
        label-cols-sm="3"
        label-align-sm="right"
        label-size="sm"
        label-for="filterInput"
        class="mb-0 col-12"
      >
        <b-input-group class="col-12" size="sm">
          <b-form-input
            v-model="filter"
            type="search"
            id="filterInput"
            placeholder="Type to Search"
          ></b-form-input>
          <b-input-group-append>
            <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
          </b-input-group-append>
          <b-form-checkbox-group v-model="filterOn" class="mt-1 col-6">
            <b-form-checkbox value="kor_name">이름</b-form-checkbox>
            <b-form-checkbox value="department">부서</b-form-checkbox>
          </b-form-checkbox-group>
        </b-input-group>
      </b-form-group>
    </b-col>

    <!-- Main table element -->
    <b-table
      small
      id="my-table"
      stacked="md"
      :items="items"
      :fields="fields"
      :filterIncludedFields="filterOn"
      :current-page="currentPage"
      :per-page="perPage"
      :filter="filter"
      @filtered="onFiltered"
    >

      <template v-slot:cell(actions)="row">
                <base-button type="info" size="sm" icon @click="listModal(row.item)">
                    <i class="tim-icons icon-bullet-list-67"></i>
                </base-button>
                <base-button type="success" size="sm" icon @click="edit(row.item)">
                    <i class="tim-icons icon-settings"></i>
                </base-button>
                <base-button type="danger" size="sm" icon @click="deleteModal(row.item)">
                    <i class="tim-icons icon-simple-remove"></i>
                </base-button>
                <base-button type="primary" size="sm" icon @click="cameraModal(row.item)">
                    <i class="tim-icons icon-camera-18"></i>
                </base-button>
      </template>

      <template v-slot:row-details="row">
        <b-card>
          <ul>
            <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
          </ul>
        </b-card>
      </template>
    </b-table>
    <base-button type="info" fill size="sm" style="float:right; margin-right: 25px" @click="modals.modal1 = true">추가</base-button>
    <div slot="footer">
        <b-pagination align=center size="sm" v-model="currentPage" :total-rows="totalRows" :per-page="perPage" aria-controls="my-table">
        </b-pagination>
    </div>
    <!-- 생성 modal -->
    <modal :show.sync="modals.modal1"
            body-classes="p-0"
            modal-classes="modal-sm">
        <insert-worker :model="createModel"></insert-worker>
        <template slot="footer">
            <base-button type="primary" @click="realCreate()">추가</base-button>
            <base-button type="secondary" class="ml-auto" @click="closeModal1()">취소
            </base-button>
        </template>
    </modal>
    <!-- 수정 modal -->
    <modal :show.sync="modals.modal2"
            body-classes="p-0"
            modal-classes="modal-sm">
        <edit-worker :model="editModal"></edit-worker>
        <template slot="footer">
            <base-button type="primary" @click="realEdit()">수정</base-button>
            <base-button type="secondary" class="ml-auto" @click="closeModal2()">취소
            </base-button>
        </template>
    </modal>
    <!-- 제거 modal -->
    <modal :show.sync="modals.modal3"
            body-classes="p-0"
            modal-classes="modal-sm">
        <h3 slot="header" class="modal-title" id="modal-title-default" style="color: rgba(255,255,255,0.8)">사원 정보 삭제</h3>
        <hr/>
        <h4 class="text-center" style="color: rgba(255,255,255,0.8)"> 정말로 삭제하시겠습니까? </h4>
        <template slot="footer">
            <base-button type="primary" @click="realDelete()">삭제</base-button>
            <base-button type="secondary" class="ml-auto" @click="closeModal3()">취소
            </base-button>
        </template>
    </modal>

    <!-- 사진 modal -->
    <modal :show.sync="modals.modal4"
            body-classes="p-0"
            modal-classes="modal-sm">
      <card class="text-center">
        <h3 slot="header" class="title">{{addCameraPerson.kor_name}}님의 사진추가</h3>
        <img class="img-fluid" style="-webkit-user-select: none;margin: auto;" src="http://ssafyteam7.iptime.org:8090/video_feed"/>
      </card>
      <template slot="footer">
        <base-button type="secondary" class="ml-auto" @click="closeModal4()">닫기
        </base-button>
      </template>
    </modal>

    <!-- 로그 리스트 modal -->
    <modal :show.sync="modals.modal5"
            body-classes="p-0"
            modal-classes="modal-sm">
      <card class="text-center" >
        <h3 slot="header" class="title">출퇴근 리스트</h3>
        <list-person style="max-height: 200px; overflow-y: auto" :model="listModel"></list-person>
      </card>
      <template slot="footer">
        <base-button type="secondary" class="ml-auto" @click="closeModal5()">확인
        </base-button>
      </template>
    </modal>

    <!-- 확인 메시지 -->
    <modal :show.sync="modals.modal6"
            body-classes="p-0"
            modal-classes="modal-sm">
      <h3 slot="header" class="modal-title" id="modal-title-default" style="color: rgba(255,255,255,0.8)">주의사항</h3>
        <hr/>
        <h4 class="text-center" style="color: rgba(255,255,255,0.8)"> 원래 있던 사진이 삭제됩니다. <br/> 정말로 사진 찍으시겠습니까? </h4>
        <template slot="footer">
            <base-button type="primary" @click="realShoot()">촬영</base-button>
            <base-button type="secondary" class="ml-auto" @click="closeModal6()">취소
            </base-button>
        </template>
    </modal>

  </card>
</template>

<script>
/* eslint-disable */
  import InsertWorker from "@/pages/Worker/InsertWorker"
  import EditWorker from "@/pages/Worker/EditWorker"
  import ListPerson from "@/pages/Worker/ListPerson"
  import {Modal} from '@/components'
  import axios from 'axios'

  export default {
    components: {
        InsertWorker,
        Modal,
        EditWorker,
        ListPerson
    },
    data() {
      return {
        modals: {
            modal1: false,
            modal2: false,
            modal3: false,
            modal4: false,
            modal5: false,
            modal6: false
        },
        items: [],
        fields: [
          { key: 'kor_name', label: '이름', sortable: true, sortDirection: 'desc' },
          { key: 'department', label: '부서', sortable: true, class: 'text-center' },
          {
            key: 'position',
            label: '직책',
            sortable: false,
          },
          { key: 'actions', label: 'Actions' }
        ],
        totalRows: 1,
        currentPage: 1,
        perPage: 5,
        pageOptions: [5, 10, 15],
        sortBy: '',
        sortDesc: false,
        sortDirection: 'asc',
        filter: null,
        filterOn: 'kor_name',
        infoModal: {
          id: 'info-modal',
          title: '',
          content: ''
        },
        editModal: {},
        createModel : { pin: 1234},
        deleteId : '',
        addCameraPerson : {},
        listModel: [],
      }
    },
    computed: {
      sortOptions() {
        // Create an options list from our fields
        return this.fields
          .filter(f => f.sortable)
          .map(f => {
            return { text: f.label, value: f.key }
          })
      }
    },
    created() {
      // Set the initial number of items
      this.loadWorker()
    },
    methods: {
      loadWorker(){
        axios.get(`http://i3a207.p.ssafy.io:8000/blog/api/group/`)
          .then(({ data }) => {
            this.items = data
            this.totalRows = this.items.length
          })
      },
      onFiltered(filteredItems) {
        // Trigger pagination to update the number of buttons/pages due to filtering
        this.totalRows = filteredItems.length
        this.currentPage = 1
      },
      deleteModal(item){
          this.modals.modal3 = true
          this.deleteId = item.id
      },
      edit(item){
        let temp = Object.assign({}, item)
        this.editModal = temp
        this.modals.modal2 = true
      },
      cameraModal(item){
        this.addCameraPerson = item
        this.modals.modal6 = true
      },
      listModal(item){
        this.listModel = []
        axios.get(`http://i3a207.p.ssafy.io:8000/blog/api/v2/${item.id}`)
          .then(({data}) => {
            if(data.length == 0)
              return

            if(data.length == 1){
              if(data[0].out_at !== null){
                var outAtDate = data[0].out_at.substring(0, 4) + "년 " + data[0].out_at.substring(5, 7) + "월 " + data[0].out_at.substring(8, 10) + "일 " + data[0].out_at.substring(11, 19)
                var outAtStr = '외출'
                // 6시 이후면 퇴근
                var outAtHour = parseInt(data[0].out_at.substring(11, 13))
                if(outAtHour >= 18)
                  outAtStr = '퇴근'
                this.listModel.push({ time: outAtDate, action: outAtStr})
              }
              var enterAtDate = data[0].enter_at.substring(0, 4) + "년 " + data[0].enter_at.substring(5, 7) + "월 " + data[0].enter_at.substring(8, 10) + "일 " + data[0].enter_at.substring(11, 19)
              var enterAtStr = '출근'
              if(data[0].out_at === null)
                enterAtStr = '재실중'
              this.listModel.push({time : enterAtDate, action : enterAtStr})
            }

            else{
              var firstMonth = parseInt(data[0].enter_at.substring(5, 7))
              var firstDay = parseInt(data[0].enter_at.substring(8, 10))

              var preMonth = parseInt(data[1].enter_at.substring(5, 7))
              var preDay =  parseInt(data[1].enter_at.substring(8, 10))

              var isWork = false, isOffWork = false, firstColumn = false

              var saveDate = new Date(2000, firstMonth, firstDay)
              
              var preDate = new Date(2000, preMonth, preDay)

              var outAtDate, outAtStr, enterAtDate, enterAtStr

              if(data[0].out_at !== null){
                outAtDate = data[0].out_at.substring(0, 4) + "년 " + data[0].out_at.substring(5, 7) + "월 " + data[0].out_at.substring(8, 10) + "일 " + data[0].out_at.substring(11, 19)
                outAtStr = '외출'
                // 6시 이후면 퇴근
                var outAtHour = parseInt(data[0].out_at.substring(11, 13))
                if(outAtHour >= 18)
                  outAtStr = '퇴근'
                this.listModel.push({ time: outAtDate, action: outAtStr})
              }

              if(preDate.getTime() != saveDate.getTime()){
                isWork = true
                saveDate = preDate
                firstColumn = true
              }
              else{
                if(firstColumn){
                  isOffWork = true
                  firstColumn = false
                }
              }

              enterAtDate = data[0].enter_at.substring(0, 4) + "년 " + data[0].enter_at.substring(5, 7) + "월 " + data[0].enter_at.substring(8, 10) + "일 " + data[0].enter_at.substring(11, 19)
              enterAtStr = '입실'
              if(isWork){
                enterAtStr = '출근'
                firstColumn = true
              }
              if(data[data.length-1].out_at === null)
                enterAtStr = '재실중'
              this.listModel.push({ time: enterAtDate, action: enterAtStr})


              for(let i = 1; i< data.length - 1; i++){
                isWork = false
                isOffWork = false
                preMonth = parseInt(data[i+1].enter_at.substring(5, 7))
                preDay = parseInt(data[i+1].enter_at.substring(8, 10))
                preDate = new Date(2000, preMonth, preDay)

                if(preDate.getTime() != saveDate.getTime()){
                  isWork = true
                  saveDate = preDate
                  firstColumn = true
                }
                else{
                  if(firstColumn){
                    isOffWork = true
                    firstColumn = false
                  }
                }

                if(data[i].out_at !== null){
                  outAtDate = data[i].out_at.substring(0, 4) + "년 " + data[i].out_at.substring(5, 7) + "월 " + data[i].out_at.substring(8, 10) + "일 " + data[i].out_at.substring(11, 19)
                  outAtStr = '외출'
                  if(isOffWork)
                    outAtStr = '퇴근'
                  this.listModel.push({ time: outAtDate, action: outAtStr})
                }
                enterAtDate = data[i].enter_at.substring(0, 4) + "년 " + data[i].enter_at.substring(5, 7) + "월 " + data[i].enter_at.substring(8, 10) + "일 " + data[i].enter_at.substring(11, 19)
                enterAtStr = '입실'
                if(isWork)
                  enterAtStr = '출근'
                this.listModel.push({ time: enterAtDate, action: enterAtStr})
              }

              // 마지막 타임 스템프
              if(data[data.length-1].out_at !== null){
                outAtDate = data[data.length-1].out_at.substring(0, 4) + "년 " + data[data.length-1].out_at.substring(5, 7) + "월 " + data[data.length-1].out_at.substring(8, 10) + "일 " + data[data.length-1].out_at.substring(11, 19)
                outAtStr='외출'
                if(firstColumn)
                  outAtStr = '퇴근'
                this.listModel.push({ time: outAtDate, action: outAtStr})
              }

              enterAtDate = data[data.length-1].enter_at.substring(0, 4) + "년 " + data[data.length-1].enter_at.substring(5, 7) + "월 " + data[data.length-1].enter_at.substring(8, 10) + "일 " + data[data.length-1].enter_at.substring(11, 19)
              enterAtStr = '출근'
              this.listModel.push({ time: enterAtDate, action: enterAtStr})
            }
          })
        this.modals.modal5 = true
      },
      closeModal1(){
        this.createModel = { pin: 1234 }
        this.modals.modal1 = false
      },
      closeModal2(){
        this.editModal = {}
        this.modals.modal2 = false
      },
      closeModal3(){
        this.modals.modal3 = false
        this.deleteId = ''
      },
      closeModal4(){
        this.modals.modal4 = false
        this.addCameraPerson = {}
      },
      closeModal5(){
        this.modals.modal5 = false
      },
      closeModal6(){
        this.modals.modal6 = false
        this.addCameraPerson = {}
      },
      realCreate(){
        axios.post(`http://i3a207.p.ssafy.io:8000/blog/api/group/`, this.createModel)
          .then(() => {
            this.loadWorker()
            this.modals.modal1 = false
            this.createModel = { pin: 1234 }
          })
          .catch(error => {
            console.log(error.message)
          })
      },
      realEdit(){
        axios.put(`http://i3a207.p.ssafy.io:8000/blog/api/group/${this.editModal.id}`, this.editModal)
          .then(() => {
            this.loadWorker()
            this.modals.modal2 = false
          })
          .catch(error => {
            console.log(error.message)
          })
      },
      realDelete(){
        axios.delete(`http://i3a207.p.ssafy.io:8000/blog/api/group/${this.deleteId}`)
          .then(()=> {
            this.loadWorker()
            this.modals.modal3 = false
          })
          .catch(error => {

          })
      },
      realShoot(){
        this.modals.modal4 = true
        this.modals.modal6 = false
        axios.get(`http://i3a207.p.ssafy.io:8000/blog/api/camera/${this.addCameraPerson.id}`)
          .then(() => {
            this.loadWorker()
          })
          .catch(error => {
            console.log(error.message)
          })
      },
    }
  }
</script>