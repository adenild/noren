let inflows = new Vue({
    el: '#inflows',
    data: function () {
        return {
            operations: null,
            wallets: null,
        }
    },

    methods: {
        getCookie: function (name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                let cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    let cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },

        loadOperations: async function () {
            let scope = this;
            const params = {"operation": "+"};
            $.ajax({
                method: "POST",
                url: "load/",
                data: params,
                headers: {'X-CSRFToken': this.getCookie("csrftoken")}
            }).then(response => scope.operations = response)
                // .catch(error => scope.booleans.failed = true)
        },

        loadWallets: async function() {
            let scope = this;
            $.ajax({
                method: "GET",
                url: "/wallet/load/",
                headers: {'X-CSRFToken': this.getCookie("csrftoken")}
            }).then(response => scope.wallets = response)
        }
    },

    filters: {
        formatDate: function (value) {
            if (!value) return ''
            value = moment(value).format("DD/MM/YYYY")
            return value
        }
    },

    mounted: function () {
        this.loadOperations();
        this.loadWallets();
    }
});