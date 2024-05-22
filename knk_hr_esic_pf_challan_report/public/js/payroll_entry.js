frappe.ui.form.on('Payroll Entry', {
    refresh: function(frm) {
		var me = this;
        let doc = frm.doc;
        if(!frm.doc.custom_pf_challan_done){
            frm.add_custom_button('Generate PF Challan', function() {
    			frm.trigger("create_pf_details");
    		}, 'Create');
        }
	},
	create_pf_details() {
	    cur_frm.call({
          method: "knk_hr_esic_pf_challan_report.overrides.custom_payroll_entry.create_pf_details",
          args: {
             "payroll_entry": cur_frm.doc.name
          },
          callback: function(r) {
            if(r.message)
                console.log('Successfully generated PF File.');
          }
         });
	},
})