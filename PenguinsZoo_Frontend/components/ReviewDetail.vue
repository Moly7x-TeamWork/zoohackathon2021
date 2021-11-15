<template>
    <div>
        <div class="mx-12 flex border border-yellow-500 rounded-lg">
            <div class="px-7 py-5 w-11/12">
                <div class="flex">
                    <h1 class="font-semibold mr-2">Link group:</h1>
                    <a
                        class="text-green-700 hover:text-yellow-600"
                        target="_blank"
                        :href="report.linkGroup"
                        >{{ report.linkGroup }}</a
                    >
                </div>

                <h1 class="font-semibold">Report summarization:</h1>
                <div>
                    <p class="px-5 py-2">{{ report.summary }}</p>
                </div>

                <div class="flex">
                    <h1 class="mr-2 font-semibold">Status:</h1>
                    <p v-for="currStatus in $store.state.review.statusReport">
                        <span v-if="report.status === currStatus.id">{{
                            currStatus.label
                        }}</span>
                    </p>
                </div>
            </div>
            <div class="flex flex-col w-1/12 justify-center">
                <div @click="acceptGroup(report.id)">
                    <Check
                        class="cursor-pointer mb-3"
                        :class="isAccept ? 'accept' : ''"
                    ></Check>
                </div>
                <div @click="denyGroup(report.id)">
                    <Delete
                        class="cursor-pointer"
                        :class="isDeny ? 'deny' : ''"
                    ></Delete>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Check from '~/static/Check'
import Delete from '~/static/Delete'
import Swal from 'sweetalert2'
import VueCookies from 'vue-cookies'
export default {
    components: { Delete, Check },
    props: {
        report: Object,
    },
    data() {
        return {
            isAccept: false,
            isDeny: false,
            currentId: 0,
            currentStatus: 2,
        }
    },
    methods: {
        acceptGroup(id) {
            this.isAccept = true
            this.isDeny = false
            this.currentId = id
            this.currentStatus = 2
            this.reviewReport()
        },

        denyGroup(id) {
            this.isAccept = false
            this.isDeny = true
            this.currentId = id
            this.currentStatus = 3
            this.reviewReport()
        },

        reviewReport() {
            const reviewPayload = {
                idGroup: this.currentId,
                idUser: VueCookies.get('id'),
                status: this.currentStatus,
            }
            const self = this
            this.$store
                .dispatch('review/changeStatus', reviewPayload)
                .then((response) => {
                    Swal.fire({
                        title: 'Thông báo',
                        text: response.data.msg,
                        showConfirmButton: false,
                        timer: 1500,
                        icon: 'success',
                    })
                })
        },
    },
}
</script>

<style scoped>
.accept {
    fill: #41b883;
}

.deny {
    fill: #ff0000;
}
</style>
