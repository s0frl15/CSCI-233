CREATE DATABASE IF NOT EXISTS bug_collector;

CREATE TABLE IF NOT EXISTS bug_collector.IT_employee (
  `emp_num` varchar(20) NOT NULL,
  `emp_name` varchar(20) NOT NULL,
  `emp_dept` varchar(12) NOT NULL,
  `emp_email` varchar(20) NOT NULL,
  PRIMARY KEY (`emp_num`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS bug_collector.agent (
  `agent_emp_num` varchar(30) NOT NULL,
  `agent_name` varchar(30) NOT NULL,
  `agent_email` varchar(30) NOT NULL,
  `agent_dept` varchar(20) NOT NULL,
  `agent_phone` int NOT NULL,
  PRIMARY KEY (`agent_emp_num`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS bug_collector.report (
  `report_number` int NOT NULL AUTO_INCREMENT,
  `agent_emp_num` varchar(30) NOT NULL,
  `emp_num` varchar(30) NOT NULL,
  `platform` varchar(30) NOT NULL,
  `software_name` varchar(30) NOT NULL,
  `error_type` varchar(45) NOT NULL,
  `impact` varchar(30) NOT NULL,
  `time_stamp` varchar(25) NOT NULL,
  `description` varchar(1000) NOT NULL,
  PRIMARY KEY (`report_number`),
  KEY `fk_agent_emp_num(agent_emp_num)<-agent(agent_emp_num)_idx` (`agent_emp_num`),
  KEY `fk_emp_num(emp_num)<-IT_employee(emp_num)_idx` (`emp_num`),
  CONSTRAINT `fk_agent_emp_num(agent_emp_num)<-agent(agent_emp_num)` FOREIGN KEY (`agent_emp_num`) REFERENCES `agent` (`agent_emp_num`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_emp_num(emp_num)<-IT_employee(emp_num` FOREIGN KEY (`emp_num`) REFERENCES `it_employee` (`emp_num`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;