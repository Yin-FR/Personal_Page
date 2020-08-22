import {CHANGE_PAGE, FIND_DEVICE} from "./mutation-type";

export default {
    findDevice({commit}, index){
        commit(FIND_DEVICE, index)
    },
    changePage({commit}, index){
        commit(CHANGE_PAGE, {index})
    }
}