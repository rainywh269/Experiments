/*
 * script.js
 * Copyright (C) 2013 wooparadog <wooparadog@1l0v3U4v3r>
 *
 * Distributed under terms of the MIT license.
 */

$(function(){
    $("form").submit(function(e){
        e.preventDefault();
        var $this=$(this), section=$this.parents("li.sub-section"),
            section_id=section.data('section-id'),
            text=$this.find("input[name=text]").val();

        $.post(
            "/form/url",
            {
                text: text
            },
            function(data){
                alert(1);
            });
    });
});

