y=0;
height=$("#ulist").height();
$("#scrollMagic").mousewheel(
        function(event, delta, deltaX, deltaY) {
            y+=104*delta;
            if(y>0)y=0;
	    max_top=($("#ulist > *").length-3)*104;
	    if(max_top<0&&delta>0)max_top=0;
            if(y<-max_top&&delta<0)y=-max_top;
            $("#ulist").animate( { top:y+"px"}, { queue:false, duration:500 } );
        }
        );
