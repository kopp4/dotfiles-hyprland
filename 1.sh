git filter-branch --commit-filter '
    if [ "$GIT_AUTHOR_EMAIL" = "taltalasuka@qq.com" ];
    then
        GIT_AUTHOR_EMAIL="kopp4@users.noreply.github.com";
    fi;
    git commit-tree "$@";
    ' HEAD

