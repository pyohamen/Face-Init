// store/index.js

import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const resourceHost = 'http://i3a207.p.ssafy.io:8000'

const enhanceAccessToken = () => {
    const { accessToken } = localStorage
    if (accessToken == undefined) return
    axios.defaults.headers.common['Authorization'] = `Token ${accessToken}`;
}
enhanceAccessToken()

export default new Vuex.Store({
    state: {
        accessToken: null
    },
    getters: {
        isAuthenticated: function (state) {
            if (state.accessToken == null)
                return false
            else
                return true
        }
    },
    mutations: {
        LOGIN(state, { token }) {
            state.accessToken = token

            localStorage.accessToken = token
        },
        LOGOUT(state) {
            state.accessToken = null
            delete localStorage.accessToken
        }
    },
    actions: {
        LOGIN({ commit }, { username, password }) {
            return axios.post(`${resourceHost}/token/`, { username, password })
                .then(({ data }) => {
                    commit('LOGIN', data)

                    axios.defaults.headers.common['Authorization'] = `Token ${data.token}`
                })
                .catch(error => {
                    alert("아이디 또는 비밀번호가 틀렸습니다.")
                })
        },
        LOGOUT({ commit }) {
            axios.defaults.headers.common['Authorization'] = undefined
            commit('LOGOUT')
        },
    }
})