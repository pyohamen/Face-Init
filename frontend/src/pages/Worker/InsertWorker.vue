<template>
  <div class="row">
    <div class="col-md-12">
      <card>
        <h5 slot="header" class="title">사원 추가</h5>
        <div class="row">
          <div class="col-md-6 pr-md-1">
            <base-input label="이름"
                        placeholder="예) 홍길동"
                        v-model="model.kor_name">
            </base-input>
          </div>
          <div class="col-md-6 pr-md-1">
            <base-input label="영어 이름"
                        placeholder="예) Gildong"
                        v-model="model.eng_name">
            </base-input>
          </div>
        </div>
        <div class="row">
          <div class="col-md-7 pr-md-1">
            <base-input label="부서"
                        v-model="model.department">
              <select id="inputState" class="form-control" v-model="model.department">
                <option v-for="listValue in departmentList" :value="listValue" :key="listValue">
                  {{listValue}}
                </option>
              </select>
            </base-input>
          </div>
          <div class="col-md-5 pr-md-1">
            <base-input label="직책">
              <select id="inputState" class="form-control" v-model="model.position">
                <option v-for="listValue in positionList" :value="listValue" :key="listValue">
                  {{listValue}}
                </option>
              </select>
            </base-input>
          </div>
        </div>
      </card>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
  export default {
    props: {
      model: {
        type: Object,
        default: () => {
          return {};
        }
      }
    },
    data() {
      return {
        positionList : ['사원', '주임', '대리', '과장', '차장', '부장', '이사', '상무', '전무', '부사장', '사장', '부회장', '회장'],
        departmentList : ['총무부', '경리부', '구매자제부', '품질관리부', '상품관리부', '기술부', '국내영업부', '해외영업부', '고객관리부', '개발부'],
      }
    },
    watch: {
      'model.eng_name' : function(val){
        const reg = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;

        if(reg.exec(val)!==null){
          return this.model.eng_name = this.model.eng_name.slice(0, -1);
        }
      },
      'model.kor_name' : function(val){
        const reg = /[a-z]/;

        if(reg.exec(val)!== null){
          return this.model.kor_name = this.model.kor_name.slice(0, -1);
        }
      }
    }
  }
</script>
<style>
option {
  color : rgb(0, 0, 0)
}
</style>