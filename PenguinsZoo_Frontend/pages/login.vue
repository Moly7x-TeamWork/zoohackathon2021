<template class="h-full">
    <div class="bg-primary flex justify-center h-full opacity-90">
        <div class="flex mt-20 bg-white w-4/6 h-3/4 rounded-lg flex-wrap">
            <div class="w-1/2">
                <div class="ml-3 mt-6 relative">
                    <img src="../static/logo4.jpg" class="absolute" />
                </div>
            </div>
            <div class="w-1/2 mt-5">
                <div class="flex justify-end">
                    <NuxtLink to="/" class="text-green-700 flex mr-5"
                        ><Back class="pt-2"></Back> Home</NuxtLink
                    >
                </div>
                <div class="text-center">
                    <h1 class="font-semibold text-3xl mt-12 mr-5 text-card">
                        Sign in
                    </h1>
                </div>

                <div class="mt-3 pl-10">
                    <h1 class="font-semibold">Username:</h1>
                    <div class="mt-1 w-10/12">
                        <t-input
                            v-model="username"
                            placeholder="Input the username"
                        ></t-input>
                    </div>
                </div>
                <div class="mt-3 pl-10">
                    <h1 class="font-semibold">Password:</h1>
                    <div class="mt-1 w-10/12">
                        <t-input
                            type="password"
                            v-model="password"
                            placeholder="Input the password"
                            @keyup.enter="signIn"
                        ></t-input>
                    </div>
                </div>
                <div class="mt-5 text-center">
                    <button
                        @click="signIn"
                        class="
                            border border-card
                            px-5
                            py-1
                            rounded-lg
                            text-card
                            hover:bg-card hover:text-white
                        "
                    >
                        Sign in
                    </button>
                    <p class="text-gray-500 text-sm mt-3">
                        If you don't have an account sign up in
                        <span
                            class="cursor-pointer text-green-700 font-semibold"
                            >here</span
                        >
                        !
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Back from '~/static/back'
import VueCookies from 'vue-cookies'
import Swal from 'sweetalert2'
export default {
    name: 'login',
    components: { Back, VueCookies },
    data() {
        return {
            title: 'Login',
            infinite_key: '',
            username: '',
            password: '',
        }
    },
    head() {
        return {
            title: this.title,
            meta: [
                { hid: 'og-title', property: 'og:title', content: this.title },
            ],
        }
    },

    methods: {
        signIn() {
            const self = this
            this.$store.state.loading = true
            if (!this.username || !this.password) {
                Swal.fire({
                    title: 'Notification',
                    text: 'Please fill the username and password!',
                    showCancelButton: false,
                    confirmButtonText: `OK`,
                    icon: 'error',
                })
            }
            const loginPayLoad = {
                username: this.username,
                password: this.password,
            }
            this.$store
                .dispatch('home/login', loginPayLoad)
                .then((response) => {
                    console.log(response)
                    if (response.status === 200) {
                        VueCookies.set('id', response.data.id, '1h')
                        VueCookies.set('username', response.data.username, '1h')
                        Swal.fire({
                            title: 'Notification',
                            text: 'Login successful!',
                            showCancelButton: false,
                            showConfirmButton: false,
                            timer: 2000,
                            icon: 'success',
                        })
                        this.$router.push('/')
                    } else {
                        Swal.fire({
                            title: 'Notification',
                            text: 'Username or password invalid!',
                            showCancelButton: false,
                            confirmButtonText: `OK`,
                            icon: 'error',
                        })
                    }
                })
                .catch((err) => {
                    this.$store.state.loading = false
                })
        },
    },
}
</script>

<style>
html {
    height: 100%;
}

body {
    height: 100%;
}

div#__nuxt {
    height: 100%;
}

div#__layout {
    height: 100%;
}
</style>
