package org.ejkit.core;

import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.stereotype.*;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@EnableTransactionManagement
public class BaseServerApplication {

    public static void main(String[] args) throws Exception {
        SpringApplication.run(BaseServerApplication.class, args);
    }
}
