function switch_tool_bar(clicked_obj)
    {
        if(clicked_obj=="退出"){

        }
        if(clicked_obj=="项目管理"){
            document.getElementById("tool_project_namage").style.display="block";
            document.getElementById("tool_reslut_namage").style.display="none";
            document.getElementById("tool_data_analize").style.display="none";

        }
        if(clicked_obj=="贮存延寿成果管理"){
            document.getElementById("tool_project_namage").style.display="none";
            document.getElementById("tool_reslut_namage").style.display="block";
            document.getElementById("tool_data_analize").style.display="none";
        }
        if(clicked_obj=="数据分析"){
            document.getElementById("tool_project_namage").style.display="none";
            document.getElementById("tool_reslut_namage").style.display="none";
            document.getElementById("tool_data_analize").style.display="block";
        }
        if(clicked_obj=="新建工程"){

        }
        if(clicked_obj=="元器件信息管理"){

        }
        if(clicked_obj=="贮存延寿信息管理"){

        }
    }