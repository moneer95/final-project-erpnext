frappe.ui.form.on('Journal Entry', {
    onload_post_render: function(frm) {
        var options = ['Journal Entry',
                        'Bank Entry',
                        'Cash Entry',
                        'Credit Card Entry',
                        'Debit Note',
                        'Credit Note',
                        'Contra Entry',
                        'Excise Entry',
                        'Write Off Entry',
                        'Opening Entry',
                        'Depreciation Entry',
                        'Exchange Rate Revaluation',
                        'Deferred Revenue'
        ]
        frm.set_df_property('voucher_type', 'options', options);
    }
});
