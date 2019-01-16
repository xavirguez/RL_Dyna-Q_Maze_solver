function [R, T1, T2, T3] = create_environment(file_level)
    %% READING THE FILE AND OBTAINING FREE CELLS AND REWARD CELLS
    grid_size = [0,0];
    cells_free = [];
    cells_final = [];

    file_id = fopen(file_level);
    line = fgetl(file_id);
    grid_size(2) = length(line);
    c_line = 0;
    c = 0;
    while not(line == -1)
        for i=1:1:length(line)
            c = c + 1;
            if (line(i) == ' ') || (line(i) == 'P')
                cells_free = [cells_free, c];
            elseif line(i) == 'G'
                cells_free = [cells_free, c];
                cells_final = [cells_final, c];
            end
        end
        line = fgetl(file_id);
        c_line = c_line + 1;
    end
    grid_size(1) = c_line;
    gs = grid_size(1);
    fclose(file_id);
%     display(grid_size)
%     display(cells_final)
%     display(cells_free)
    
    %% OBTAINING T AND R MATRICES

    num_actions = 3;
    num_orientations = 4;
    num_states = grid_size(1)*grid_size(2)*num_orientations;

    T1_aux = zeros(num_states/num_orientations,num_states,num_orientations);
    for i=1:1:num_orientations
        if i==1
            for j=1:1:length(cells_free)
                c = 0;
                s = cells_free(j) - gs;
                for k=1:1:length(cells_free)
                    if cells_free(k)==s
                      c=1;  
                    end
                end
                if (c*s > 0)
                    T1_aux(cells_free(j),s+gs*gs*0,i) = 1;
                end
            end
        end
        if i==2
            for j=1:1:length(cells_free)
                c = 0;
                s = cells_free(j) + gs;
                for k=1:1:length(cells_free)
                    if cells_free(k)==s
                      c=1;  
                    end
                end
                if (c*s > 0)
                    T1_aux(cells_free(j),s+gs*gs*1,i) = 1;
                end
            end
        end
        if i==3
            for j=1:1:length(cells_free)
                c = 0;
                s = cells_free(j) + 1;
                for k=1:1:length(cells_free)
                    if cells_free(k)==s
                      c=1;  
                    end
                end
                if (c*s > 0)
                    T1_aux(cells_free(j),s+gs*gs*2,i) = 1;
                end
            end
        end
        if i==4
            for j=1:1:length(cells_free)
                c = 0;
                s = cells_free(j) - 1;
                for k=1:1:length(cells_free)
                    if cells_free(k)==s
                      c=1;  
                    end
                end
                if (c*s > 0)
                    T1_aux(cells_free(j),s+gs*gs*3,i) = 1;
                end
            end
        end
    end
    T1 = [T1_aux(:,:,1);T1_aux(:,:,2);T1_aux(:,:,3);T1_aux(:,:,4)];

    T2_aux = zeros(num_states/num_orientations,num_states,num_orientations);
    for i=1:1:num_orientations
        if i==1
            for j=1:1:length(cells_free)
                T2_aux(cells_free(j),num_states/num_orientations*2 + cells_free(j),i) = 1;
            end
        elseif i==2
            for j=1:1:length(cells_free)
                T2_aux(cells_free(j),num_states/num_orientations*3 + cells_free(j),i) = 1;
            end
        elseif i==3
            for j=1:1:length(cells_free)
                T2_aux(cells_free(j),num_states/num_orientations*1 + cells_free(j),i) = 1;
            end
        elseif i==4
            for j=1:1:length(cells_free)
                T2_aux(cells_free(j),num_states/num_orientations*0 + cells_free(j),i) = 1;
            end
        end
    end
    T2 = [T2_aux(:,:,1);T2_aux(:,:,2);T2_aux(:,:,3);T2_aux(:,:,4)];

    T3_aux = zeros(num_states/num_orientations,num_states,num_orientations);
    for i=1:1:num_orientations
        if i==1
            for j=1:1:length(cells_free)
                T3_aux(cells_free(j),num_states/num_orientations*3 + cells_free(j),i) = 1;
            end
        elseif i==2
            for j=1:1:length(cells_free)
                T3_aux(cells_free(j),num_states/num_orientations*2 + cells_free(j),i) = 1;
            end
        elseif i==3
            for j=1:1:length(cells_free)
                T3_aux(cells_free(j),num_states/num_orientations*0 + cells_free(j),i) = 1;
            end
        elseif i==4
            for j=1:1:length(cells_free)
                T3_aux(cells_free(j),num_states/num_orientations*1 + cells_free(j),i) = 1;
            end
        end
    end
    T3 = [T3_aux(:,:,1);T3_aux(:,:,2);T3_aux(:,:,3);T3_aux(:,:,4)];

    R_aux = -500*ones(num_states/num_orientations,num_actions,num_orientations);
    for i=1:1:length(cells_free)
        left = cells_free(i) - 1;
        for j=1:1:length(cells_free)
            if cells_free(j) == left
                R_aux(left,1,3) = -10;
            end
        end
        top = cells_free(i) - gs;
        for j=1:1:length(cells_free)
            if cells_free(j) == top
                R_aux(top,1,2) = -10;
            end
        end    
        right = cells_free(i) + 1;
        for j=1:1:length(cells_free)
            if cells_free(j) == right
                R_aux(right,1,4) = -10;
            end
        end    
        bottom = cells_free(i) + gs;
        for j=1:1:length(cells_free)
            if cells_free(j) == bottom
                R_aux(bottom,1,1) = -10;
            end
        end
    end

    for i=1:1:num_orientations
        for j=1:1:length(cells_free)
            R_aux(cells_free(j),2,i) = -10;
            R_aux(cells_free(j),3,i) = -10;
        end
    end

    for i=1:1:length(cells_final)
        R_aux(cells_final(i),2:3,1) = [500,500];
        R_aux(cells_final(i),2:3,2) = [500,500];
        R_aux(cells_final(i),2:3,3) = [500,500];
        R_aux(cells_final(i),2:3,4) = [500,500];
        left = cells_final(i) - 1;
        left_2 = cells_final(i) - 2;
        for j=1:1:length(cells_free)
            if cells_free(j) == left
                R_aux(left,1,3) = 500;
            end
            if cells_free(j) == left_2
                R_aux(left_2,1,3) = 100;
            end
        end
        top = cells_final(i) - gs;
        top_2 = cells_final(i) - 2*gs;
        for j=1:1:length(cells_free)
            if cells_free(j) == top
                R_aux(top,1,2) = 500;
            end
            if cells_free(j) == top_2
                R_aux(top_2,1,2) = 100;
            end
        end    
        right = cells_final(i) + 1;
        right_2 = cells_final(i) + 2;
        for j=1:1:length(cells_free)
            if cells_free(j) == right
                R_aux(right,1,4) = 500;
            end
            if cells_free(j) == right_2
                R_aux(right_2,1,4) = 100;
            end
        end    
        bottom = cells_final(i) + gs;
        bottom_2 = cells_final(i) + 2*gs;
        for j=1:1:length(cells_free)
            if cells_free(j) == bottom
                R_aux(bottom,1,1) = 500;
            end
            if cells_free(j) == bottom_2
                R_aux(bottom_2,1,1) = 100;
            end
        end
    end
    R = [R_aux(:,:,1);R_aux(:,:,2);R_aux(:,:,3);R_aux(:,:,4)];
%     mat2np(T1,'T1.pkl','float64');
%     mat2np(T2,'T2.pkl','float64');
%     mat2np(T3,'T3.pkl','float64');
%     mat2np(R,'R.pkl','float64');
    save(strcat(file_level(1:end-3),'mat'), 'R', 'T1', 'T2', 'T3');
end