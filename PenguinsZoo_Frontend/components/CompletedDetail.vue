<template>
    <div>
        <div class="mx-12 my-5 flex border border-yellow-500 rounded-lg">
            <div class="px-7 py-5 w-11/12">
                <div class="flex">
                    <h1 class="font-semibold mr-2">Link group:</h1>
                    <a
                        class="text-blue-500 hover:text-green-500"
                        target="_blank"
                        :href="completed.linkgroup"
                        >{{ completed.linkgroup }}</a
                    >
                </div>

                <div class="flex">
                    <h1 class="mr-2 font-semibold">Status:</h1>
                    <p v-if="completed.status === 'True'">Accepted</p>
                    <p v-else>Denied</p>
                </div>

                <div class="flex">
                    <h1 class="mr-2 font-semibold">Reviewer:</h1>
                    <p>{{ completed.username }}</p>
                </div>

                <div class="flex">
                    <h1 class="mr-2 font-semibold">Review time:</h1>
                    <p>{{ completed.reviewTime }}</p>
                </div>

                <div class="flex">
                    <h1 class="mr-5 font-semibold">Report details:</h1>
                    <div>
                        <div v-for="(report, index) in completed.link">
                            <a
                                :href="'https://' + report.linkUser"
                                target="_blank"
                                class="mr-5 text-yellow-500 hover:text-blue-500"
                                >Link facebook of user {{ index + 1 }}</a
                            >
                            <a
                                :href="report.linkFull"
                                target="_blank"
                                class="text-card hover:text-blue-500"
                                >All posts of user {{ index + 1 }}</a
                            >
                        </div>
                    </div>
                </div>

                <div class="mt-4 flex">
                    <div v-for="(stat, index) in completed.stats">
                        <p
                            v-if="index == 1"
                            class="
                                border
                                bg-red-500
                                px-12
                                py-1
                                rounded-full
                                mr-2
                                font-semibold
                                text-white
                            "
                        >
                            1B: {{ stat }}
                        </p>
                        <p
                            v-if="index == 2"
                            class="
                                border
                                bg-yellow-500
                                px-12
                                py-1
                                rounded-full
                                mr-2
                                font-semibold
                                text-white
                            "
                        >
                            2B: {{ stat }}
                        </p>
                        <p
                            v-if="index == 3"
                            class="
                                border
                                bg-yellow-400
                                px-12
                                py-1
                                rounded-full
                                font-semibold
                                text-white
                            "
                        >
                            Others: {{ stat }}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Check from '~/static/Check'
import Delete from '~/static/Delete'
import Swal from 'sweetalert2'
export default {
    components: { Delete, Check },
    props: {
        completed: Object,
    },
    data() {
        return {
            isAccept: false,
            isDeny: false,
        }
    },
    methods: {},
}
</script>

<style scoped></style>
