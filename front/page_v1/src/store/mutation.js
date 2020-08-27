import {
    CHANGE_PAGE,
    FIND_DEVICE
} from "./mutation-type";

export default {
    [FIND_DEVICE](state, {index}){
        function _isMobile() {
            let flag = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i)
            return flag;
        }
        let _device = _isMobile();
        if (_device){
            if (_device[0] === 'Pad' || _device[0] === 'iPad'){
                state.device = 'pad'
            } else {
                state.device = 'mobile'
            }
        } else {
            state.device = 'pc'
        }
    },
    [CHANGE_PAGE](state, {index}){
        state.pageSelect = index.page;
    }
}