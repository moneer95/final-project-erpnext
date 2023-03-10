frappe.ui.form.on('Payment Entry', {
    onload_post_render: function(frm) {
        var options = ['GSG-JV-.YYYY.-']
        frm.set_df_property('naming_series', 'options', options);
    }
});