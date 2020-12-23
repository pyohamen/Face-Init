import { BaseInput, Card, BaseDropdown, BaseButton, BaseCheckbox, BaseTable } from "../components/index";
/**
 * You can register global components here and use them as a plugin in your main Vue instance
 */

import { ValidationProvider, ValidationObserver } from 'vee-validate';

const GlobalComponents = {
  install(Vue) {
    Vue.component(BaseInput.name, BaseInput)
    Vue.component(Card.name, Card)
    Vue.component(BaseDropdown.name, BaseDropdown)
    Vue.component(BaseButton.name, BaseButton)
    Vue.component(BaseCheckbox.name, BaseCheckbox)
    Vue.component(BaseTable.name, BaseTable)
    Vue.component('ValidationProvider', ValidationProvider)
    Vue.component('ValidationObserver', ValidationObserver)
  }
};

export default GlobalComponents;
