function Resize()
    {
      windowW=($(window).width()-120);
      windowH=($(window).height()-100);
      $(".weingutcontainer").width(windowW).height(windowH);
      $(".lagecontainer").width(windowW).height(windowH);
      $(".newscontainer").width(windowW).height(windowH);
      $(".homecontainer").width($(window).width()).height($(window).height());
      $(".shopcontainer").width($(window).width()-210).height($(window).height()-60);
    }
    $(document).ready(Resize);
