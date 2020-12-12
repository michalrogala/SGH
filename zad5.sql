CREATE OR REPLACE PROCEDURE new_salary (p_job_id NUMBER, P_NEW_SALARY NUMBER)
IS
    NEW_SAL_TOO_LOW exception;
    salary_lower_than_zero exception;
    deadlock_detected exception;
    pragma exception_init (deadlock_detected, -60);
    v_current_sal  number(10);
    v_new_sal      number(10);
begin
    if p_new_sal < 0 then
      raise salary_lower_than_zero;
    end if;

    select salary into v_current_sal
    from employees
    where job_id = p_job_id;

    if P_NEW_SALARY >= v_current_sal then
      v_new_sal := P_NEW_SALARY;
    else
      v_new_sal := P_NEW_SALARY;
    end if;

    update employees
    set salary = v_new_sal
    where job_id = p_job_id;

    commit;
exception
    when salary_lower_than_zero then
      rollback;
      dbms_output.put_line('Salary lower, than 0');
    WHEN NEW_SAL_TOO_LOW THEN
      rollback;
      dbms_output.put_line("New salary lower than old ");
    WHEN NO_DATA_FOUND then
      rollback;
      dbms_output.put_line("Employee does not exist");
    WHEN deadlock_detected THEN
      rollback;
      dbms_output.put_line("Deadlock detected");
    WHEN OTHERS THEN
      rollback;
      dbms_output.put_line("Other error");
END;

