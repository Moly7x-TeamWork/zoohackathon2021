<template>
    <div class="h-full relative">
        <img
            class="absolute z-10 max-h-full w-full"
            src="../static/elephant-back2.png"
        />
        <div
            class="
                absolute
                mt-4
                ml-3
                px-2
                pt-1
                lg:mt-24 lg:ml-10
                z-40
                border
                rounded-lg
                lg:px-10 lg:py-5
                send-form
                shadow-lg
            "
        >
            <div class="text-brown-500 font-semibold lg:text-3xl flex">
                <p class="mr-2 lg:mr-5">Send your report link</p>
                <Email36
                    style="fill: #041404; width: 30px"
                    class="animate-bounce"
                ></Email36>
            </div>
            <t-input
                @keyup.enter="addLink"
                class="lg:mt-5"
                v-model="link"
                placeholder="Link"
            ></t-input>
            <button
                @click="addLink"
                class="
                    px-2
                    py-1
                    my-1
                    ml-20
                    lg:ml-32 lg:mt-3 lg:px-5 lg:py-1
                    border border-hover
                    rounded-lg
                    text-white
                    font-semibold
                    hover:bg-hover
                "
            >
                Send
            </button>
        </div>
        <div class="absolute right-0 mt-44 mr-1 lg:mt-72 lg:mr-10 z-50">
            <p class="text-brown-500 font-semibold text-sm lg:text-3xl">
                ... and save our world!
            </p>
        </div>
    </div>
</template>
s
<style>
.send-text {
    background-color: #d8c1bb;
}
</style>
<script>
import Email from '~/static/Email'
import Email36 from '~/static/Email36'
import Swal from 'sweetalert2'
export default {
    components: { Email36, Email },
    data() {
        return {
            link: '',
        }
    },
    methods: {
        addLink() {
            const linkPayload = {
                linkGroup: this.link,
            }
            this.$store
                .dispatch('home/addLinkGroup', linkPayload)
                .then((response) => {
                    console.log(response)
                    if (response.status === 200) {
                        Swal.fire({
                            title: 'Notification',
                            text: 'Thanks for your contribution',
                            showCancelButton: false,
                            showConfirmButton: false,
                            timer: 2000,
                            icon: 'success',
                        })
                        this.link = ''
                    } else {
                        Swal.fire({
                            title: 'Notification',
                            text: response.data.message,
                            showCancelButton: false,
                            confirmButtonText: `OK`,
                            icon: 'error',
                        })
                        this.link = ''
                    }
                })
                .catch((error) => {
                    Swal.fire({
                        title: 'Notification',
                        text: error.response.data.message,
                        showCancelButton: false,
                        confirmButtonText: `OK`,
                        icon: 'error',
                    })
                })
        },
    },
}
</script>
