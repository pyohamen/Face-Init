<template>
    <card>
        <form @submit.prevent>
            <base-input label="Email address"
                        type="email"
                        placeholder="Enter email">
                <small slot="helperText" id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            </base-input>
            <base-input label="Password"
                        type="password"
                        placeholder="Password">
            </base-input>
            <base-checkbox>
                Option one is this 
            </base-checkbox>
            <base-button native-type="submit" type="primary">Submit</base-button>
        </form>
    </card>
</template>

<script>
    export default {
        data() {
            return {}
        }
    }
</script>

<style>
</style>