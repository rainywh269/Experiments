/*
 * script.js
 * Copyright (C) 2013 wooparadog <wooparadog@1l0v3U4v3r>
 *
 * Distributed under terms of the MIT license.
 */

$(function(){
    $(document).click(function(e){
        $("#post-form").hide();
    });
    $(".content-hd").click(function(e){
        e.preventDefault();
        e.stopPropagation();
        var $this=$(this), section=$this.parents("li.sub-section"),
            section_id=section.data('section-id'), post_form=$("#post-form"),
            pos = $this.offset();
        if(post_form.data('section-id') != section_id){
            post_form.find("textarea").val("");
        }
        post_form.data("section-id", section_id);
        post_form.css({
            left: pos.left,
            top: pos.top + 30
        });
        post_form.show();
    });

    $("form").click(function(e){
        e.stopPropagation();
    });

    $("form").submit(function(e){
        e.preventDefault();
        var $this=$(this), section_id=$this.data("section-id"),
            text=$this.find("textarea[name=text]").val();

        $.post(
            "/",
            {
                text: text, 
                section_id: section_id
            },
            function(data){
                console.log(section_id+text);
            });
    });
});

